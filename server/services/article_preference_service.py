from server.repos.article_preference_repo import ArticlePreferenceRepo

class ArticlePreferenceService:
    def __init__(self):
        self.repo = ArticlePreferenceRepo()

    def set_preference(self, user_id, article_id, preference):
        return self.repo.set_preference(user_id, article_id, preference)