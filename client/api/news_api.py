import requests
from client.config import API_BASE_URL

class NewsAPI:
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def _headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def get_headlines(self):
        return requests.get(f"{API_BASE_URL}/headlines", headers=self._headers())

    def get_saved_articles(self):
        return requests.get(f"{API_BASE_URL}/saved", params={"user_id": self.user_id}, headers=self._headers())

    def search_articles(self, query):
        return requests.get(f"{API_BASE_URL}/search", params={"query": query}, headers=self._headers())

    def logout(self):
        return requests.get(f"{API_BASE_URL}/logout", params={"user_id": self.user_id}, headers=self._headers())
