from server.repos.external_api_repo import ExternalAPIRepository
class APIManager:
    def __init__(self):
        self.external_api_repo = ExternalAPIRepository()

    def get_active_api(self):
        apis = self.external_api_repo.get_all_servers()
        return next((api for api in apis if api["is_active"] == 1), None)
