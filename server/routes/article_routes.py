from typing import Optional
from fastapi import APIRouter, Depends
from server.controller.article_controller import ArticleController
from server.core.jwt_utils import get_current_user

router = APIRouter(prefix="/articles", tags=["articles"])
controller = ArticleController()


@router.post("/report/{article_id}")
def report_article(article_id: int, user=Depends(get_current_user), reason: Optional[str] = None):
    return controller.report_article(article_id, user["user_id"], reason)
