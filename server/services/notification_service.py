from server.repos.category_repo import CategoryRepo
from server.repos.notification_repo import NotificationRepo


class NotificationService:
    def __init__(self):
        self.repo = NotificationRepo()
        self.category_repo = CategoryRepo()

    def create_preference(self, user_id, preference_data):
        print(preference_data.category)
        # category_id = self.category_repo.get_category_by_name(preference_data.category)["category_id"]
        # print(category_id)
        return self.repo.insert_preference(user_id, preference_data)

    def get_preferences(self, user_id):
        return self.repo.get_preferences_by_user(user_id)

    def update_preference(self, user_id, preference_id, preference_data):
        return self.repo.update_preference(user_id, preference_id, preference_data)

    def delete_preference(self, user_id, preference_id):
        return self.repo.delete_preference(user_id, preference_id)


    def generate_notifications_for_new_articles(self):
        self.repo.insert_notifications_for_new_articles()
        print("Notifications inserted based on new articles.")