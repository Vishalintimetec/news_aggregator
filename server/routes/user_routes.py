from fastapi import APIRouter
from server.controller.user_controller import UserController

router = APIRouter()
controller = UserController()

@router.get("/headlines")
def get_headlines():
    return controller.get_headlines()

# @router.get("/headlines/filter")
# def get_headlines_by_date_range_and_category(
#     start_date: str = Query(..., description="Start date in YYYY-MM-DD"),
#     end_date: str = Query(..., description="End date in YYYY-MM-DD"),
#     category: Optional[str] = Query(None, description="Optional category")
# )
#     return controller.get_headlines_by_date_range(start_date, end_date, category)

@router.get("/saved")
def get_saved_articles(user_id: int):
    return controller.get_saved_articles(user_id)

@router.get("/search")
def search_articles(query: str):
    return controller.search_articles(query)


@router.get("/logout")
def logout_user(user_id: int):
    return controller.logout(user_id)

