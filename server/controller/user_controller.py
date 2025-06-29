from server.services.user_service import UserService

class UserController:
    def __init__(self):
        self.service = UserService()

    def get_today_headlines(self, category=None):
        return self.service.get_headlines_today(category)

    def get_headlines_by_date_range(self, start_date, end_date, category=None):
        return self.service.get_headlines_in_date_range(start_date, end_date, category)

    def get_saved_articles(self, user_id):
        return self.service.get_saved_articles(user_id)

    def save_article(self, user_id, article_id):
        return self.service.save_article(user_id, article_id)

    def delete_article(self, user_id, article_id):
        return self.service.delete_article(user_id, article_id)

    def search_articles(self, query, start_date, end_date, sort_by):
        return self.service.search_articles(query, start_date, end_date, sort_by)

    def get_notifications(self, user_id):
        return self.service.get_user_notifications(user_id)

    def logout(self, user_id):
        return self.service.logout(user_id)
