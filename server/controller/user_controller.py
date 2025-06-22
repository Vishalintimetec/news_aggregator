from server.services.user_service import UserService

class UserController:
    def __init__(self):
        self.service = UserService()

    def get_headlines(self):
        return self.service.get_latest_headlines()

    def get_saved_articles(self, user_id: int):
        return self.service.get_saved_articles(user_id)

    def search_articles(self, query: str):
        return self.service.search_articles(query)

    def get_notifications(self, user_id: int):
        return self.service.get_user_notifications(user_id)

    def logout(self, user_id: int):
        return self.service.logout(user_id)
