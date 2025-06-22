import requests
from client.config import API_BASE_URL

class AuthAPI:
    def register(self, username, email, password):
        data = {"username": username, "email": email, "password": password}
        return requests.post(f"{API_BASE_URL}/users/register", json=data)

    def login(self, email, password):
        data = {"email": email, "password": password}
        return requests.post(f"{API_BASE_URL}/users/login", json=data)
