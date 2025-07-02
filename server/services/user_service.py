from server.repos.article_repo import ArticleRepository


class UserService:
    def __init__(self):
        self.repo = ArticleRepository()

    def get_headlines_today(self, category):
        return self.repo.fetch_headlines_by_day(category)

    def get_headlines_in_date_range(self, start, end, category):
        return self.repo.fetch_headlines_in_range(start, end, category)

    def get_saved_articles(self, user_id):
        return self.repo.fetch_saved_articles(user_id)

    def save_article(self, user_id, article_id):
        return self.repo.insert_saved_article(user_id, article_id)

    def delete_article(self, user_id, article_id):
        return self.repo.remove_saved_article(user_id, article_id)

    def search_articles(self, query, start, end, sort_by):
        return self.repo.search_articles(query, start, end, sort_by)

    def logout(self, user_id):
        return {"message": f"User {user_id} logged out successfully."}



