import requests
from client.api.base import BaseAPIClient
from client.config import SERVER_URL

class AdminAPIClient(BaseAPIClient):
    def get_external_servers(self):
        return requests.get(f"{SERVER_URL}/admin/external-servers", headers=self._headers())

    def get_external_server_details(self, server_id):
        return requests.get(f"{SERVER_URL}/admin/external-servers/{server_id}", headers=self._headers())

    def update_external_server(self, server_id, api_key):
        return requests.put(f"{SERVER_URL}/admin/external-servers/{server_id}", headers=self._headers(), json={"api_key": api_key})

    def add_category(self, name):
        return requests.post(f"{SERVER_URL}/admin/categories", headers=self._headers(), json={"name": name})

    def hide_article(self, article_id, hide=True):
        return requests.put(f"{SERVER_URL}/admin/articles/{article_id}/hide", headers=self._headers(), json={"hide": hide})

    def hide_category(self, category_id, hide=True):
        return requests.put(f"{SERVER_URL}/admin/categories/{category_id}/hide", headers=self._headers(), json={"hide": hide})

    # def block_keyword(self, keyword):
    #     return requests.post(f"{SERVER_URL}/admin/keywords", headers=self._headers(), json={"keyword": keyword})
    #
    # def unblock_keyword(self, keyword):
    #     return requests.delete(f"{SERVER_URL}/admin/keywords", headers=self._headers(), json={"keyword": keyword})