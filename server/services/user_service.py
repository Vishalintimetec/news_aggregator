from server.repos.article_repo import ArticleRepository
from server.repos.saved_repo import SavedArticleRepository


class UserService:
    def __init__(self):
        self.article_repo = ArticleRepository()
        self.saved_repo = SavedArticleRepository()

    def get_latest_headlines(self):
        return self.article_repo.get_top_headlines()

    def get_saved_articles(self, user_id: int):
        return self.saved_repo.get_by_user(user_id)

    def search_articles(self, query: str):
        return self.article_repo.search_by_keyword(query)

    def logout(self, user_id: int):
        return {"message": f"User {user_id} logged out successfully."}
