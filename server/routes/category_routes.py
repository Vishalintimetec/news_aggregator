from fastapi import APIRouter, Depends
from server.schemas.category import CategoryCreate
from server.controller.category_controller import CategoryController
from server.core.jwt_utils import admin_required

controller = CategoryController()
router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/")
def add_category(category: CategoryCreate, user= Depends(admin_required)):
    return controller.create_category(category)


@router.put("/admin/category/{category_id}/visibility")
def toggle_category_visibility(category_id: int, is_visible: bool,  user= Depends(admin_required)):
    return controller.toggle_category_visibility(category_id, is_visible)
