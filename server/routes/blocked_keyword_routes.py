from fastapi import APIRouter, Depends, Query
from server.controller.blocked_keyword_controller import BlockedKeywordController
from server.core.jwt_utils import admin_required

router = APIRouter(prefix="/admin/keywords", tags=["admin-keywords"])
controller = BlockedKeywordController()

@router.post("/")
def block_keyword(keyword: str, user=Depends(admin_required)):
    return controller.add_keyword(keyword)

@router.delete("/")
def unblock_keyword(keyword: str, user=Depends(admin_required)):
    return controller.remove_keyword(keyword)

@router.get("/")
def list_blocked_keywords(user=Depends(admin_required)):
    return controller.get_all_keywords()