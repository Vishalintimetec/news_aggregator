import jwt
from client.api.auth_api import AuthAPI
from client.api.user_api import UserAPI

class APIClient:
    def __init__(self):
        self.token = None
        self.user_id = None
        self.user_role = None
        self.email = None
        self.auth = AuthAPI()
        self.user = None  # Will hold UserAPI instance after login

    def login(self, email, password):
        resp = self.auth.login(email, password)
        if resp.ok:
            self.token = resp.json()["access_token"]
            payload = jwt.decode(self.token, options={"verify_signature": False})
            self.user_id = payload.get("user_id")
            self.user_role = payload.get("role")
            self.email = payload.get("sub")
            self.user = UserAPI(self.token, self.user_id)
        return resp

    def register(self, username, email, password):
        return self.auth.register(username, email, password)
