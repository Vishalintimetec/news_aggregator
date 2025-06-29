from fastapi import APIRouter, Depends, Query
from server.controller.user_controller import UserController
from server.core.jwt_utils import get_current_user
from typing import Optional

router = APIRouter(prefix="/user", tags=["user"])
controller = UserController()

@router.get("/headlines/today")
def get_today_headlines(category: Optional[str] = None):
    return controller.get_today_headlines(category)

@router.get("/headlines/date-range")
def get_headlines_by_date_range(start_date: str = Query(...), end_date: str = Query(...), category: Optional[str] = None):
    return controller.get_headlines_by_date_range(start_date, end_date, category)

@router.get("/saved-articles")
def get_saved_articles(user=Depends(get_current_user)):
    return controller.get_saved_articles(user['user_id'])

@router.post("/saved-articles")
def save_article(article_id: int, user=Depends(get_current_user)):
    return controller.save_article(user['user_id'], article_id)

@router.delete("/saved-articles")
def delete_saved_article(article_id: int, user=Depends(get_current_user)):
    return controller.delete_article(user['user_id'], article_id)

@router.get("/search")
def search_articles(query: str, start_date: Optional[str] = None, end_date: Optional[str] = None, sort_by: Optional[str] = "likes"):
    return controller.search_articles(query, start_date, end_date, sort_by)

@router.get("/notifications")
def get_notifications(user=Depends(get_current_user)):
    return controller.get_notifications(user['user_id'])

@router.post("/logout")
def logout(user=Depends(get_current_user)):
    return controller.logout(user['user_id'])

