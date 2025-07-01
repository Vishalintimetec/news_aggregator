from server.services.user_service import UserService


class ArticleController:
    def __init__(self):
        self.user_service = UserService()

    def report_article(self, article_id, user_id, reason):
        return self.user_service.report_article(article_id, user_id, reason)
