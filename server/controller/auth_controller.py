from server.services.authentication_service import AuthService

class AuthenticationController:

    def __init__(self):
        self.authentication_service = AuthService()

    def register(self, body):
        return self.authentication_service.register_user(body)

    def login(self, body):
        return self.authentication_service.login(body)
