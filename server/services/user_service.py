from server.repos.article_repo import ArticleRepository
from server.repos.report_article_repo import ReportManager
from server.config.constants import REPORT_THRESHOLD
from server.services.email_service import EmailService

class UserService:
    def __init__(self):
        self.repo = ArticleRepository()
        self.report_manager = ReportManager()
        self.email_service = EmailService()

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


    def report_article(self, article_id, user_id, reason):
        self.report_manager.insert_report(article_id, user_id, reason)

        report_count = self.report_manager.get_report_count(article_id)
        if report_count >= REPORT_THRESHOLD:
            self.repo.hide_article(article_id)

        if report_count == 1:  # Notify only on first report
            self.email_service.send_notification_email(
                to_email="vickygaur237@gmail.com",
                message=f"Article ID {article_id} was reported by User ID {user_id}.\nReason: {reason or 'No reason provided'}.\nTotal reports: {report_count}"
            )

        return {"message": "Report submitted successfully."}
