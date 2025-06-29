import requests
import jwt
from client.config import API_BASE_URL

class AuthAPI:
    def __init__(self):
        self.token = None
        self.user_role = None
        self.email = None
        self.user_id = None

    def register(self, username, email, password):
        data = {"username": username, "email": email, "password": password}
        return requests.post(f"{API_BASE_URL}/auth/register", json=data)

    # def login(self, email, password):
    #     data = {"email": email, "password": password}
    #     resp = requests.post(f"{API_BASE_URL}/users/login", json=data)
    #     if resp.ok:
    #         self.token = resp.json()["access_token"]
    #         payload = jwt.decode(self.token, options={"verify_signature": False}, algorithms=["HS256"])
    #         self.user_role = payload.get("role")
    #         self.email = payload.get("sub")
    #         self.user_id = payload.get("user_id")
    #     return resp

    def login(self, email, password):
        data = {"email": email, "password": password}
        resp = requests.post(f"{API_BASE_URL}/auth/login", json=data)
        if resp.ok:
            json_resp = resp.json()
            print(json_resp)
            self.token = json_resp["access_token"]
            self.user_role = json_resp["role"]
            self.email = json_resp["email"]
        return resp
