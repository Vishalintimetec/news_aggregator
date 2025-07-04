from server.services.article_preference_service import ArticlePreferenceService

class ArticlePreferenceController:
    def __init__(self):
        self.service = ArticlePreferenceService()

    def set_preference(self, user_id, article_id, preference):
        return self.service.set_preference(user_id, article_id, preference)