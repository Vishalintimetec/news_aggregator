from server.repos.article_repo import ArticleRepository
from server.repos.personalization_repo import PersonalizationRepo
from server.repos.user_repository import UserRepository
from server.services.blocked_keyword_service import BlockedKeywordService


class UserService:
    def __init__(self):
        self.repo = ArticleRepository()
        self.user_repo = UserRepository()
        self.blocked_keyword_service = BlockedKeywordService()
        self.personalization_repo = PersonalizationRepo()

    def get_user_by_id(self, user_id):
        return self.user_repo.get_user_by_id(user_id)

    def filter_blocked_articles(self, articles):
        blocked_keywords = self.blocked_keyword_service.get_all_keywords()
        filtered = []
        for article in articles:
            title = (article.get('title') or '').lower()
            content = (article.get('content') or '').lower()
            if any(kw.lower() in title or kw.lower() in content for kw in blocked_keywords):
                continue
            filtered.append(article)
        return filtered

    def get_headlines_today(self, user_id):
        articles = self.repo.fetch_headlines_by_day()
        articles = self.filter_blocked_articles(articles)
        return self.personalize_articles(user_id, articles)

    def get_headlines_in_date_range(self, user_id, start, end, category):
        articles = self.repo.fetch_headlines_in_range(start, end, category)
        articles = self.filter_blocked_articles(articles)
        return self.personalize_articles(user_id, articles)

    def get_saved_articles(self, user_id):
        return self.repo.fetch_saved_articles(user_id)

    def save_article(self, user_id, article_id):
        return self.repo.insert_saved_article(user_id, article_id)

    def delete_article(self, user_id, article_id):
        return self.repo.remove_saved_article(user_id, article_id)

    def search_articles(self, user_id, query, start, end, sort_by):
        articles = self.repo.search_articles(query, start, end, sort_by)
        articles = self.filter_blocked_articles(articles)
        return self.personalize_articles(user_id, articles)

    def personalize_articles(self, user_id, articles):
        prefs = self.personalization_repo.get_notification_preferences(user_id)
        # liked = self.personalization_repo.get_liked_articles(user_id)
        liked = self.personalization_repo.get_articles_by_preference(user_id, 'like')
        disliked = self.personalization_repo.get_articles_by_preference(user_id, 'dislike')
        saved = self.personalization_repo.get_saved_articles(user_id)
        read = self.personalization_repo.get_read_history(user_id)
        personalized = []
        for article in articles:
            score = 0
            enabled_categories = [cat for cat, enabled in (prefs or {}).items() if enabled and cat != 'keywords']
            if article.get('category') in enabled_categories:
                score += 2
            keywords = (prefs.get('keywords') or []) if prefs else []
            title = (article.get('title') or '').lower()
            content = (article.get('content') or '').lower()
            if any(kw.lower() in title or kw.lower() in content for kw in keywords):
                score += 3
            if article.get('article_id') in liked:
                score += 2
            if article.get('article_id') in disliked:
                score -= 2
            if article.get('article_id') in saved:
                score += 1
            if article.get('article_id') in read:
                score += 1
            personalized.append((score, article))
        personalized.sort(reverse=True, key=lambda x: x[0])
        return [a for score, a in personalized[:20]]

    def logout(self, user_id):
        return {"message": f"User {user_id} logged out successfully."}



