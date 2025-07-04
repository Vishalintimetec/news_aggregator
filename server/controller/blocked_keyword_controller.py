from server.services.blocked_keyword_service import BlockedKeywordService

class BlockedKeywordController:
    def __init__(self):
        self.service = BlockedKeywordService()

    def add_keyword(self, keyword):
        return self.service.add_keyword(keyword)

    def remove_keyword(self, keyword):
        return self.service.remove_keyword(keyword)

    def get_all_keywords(self):
        return self.service.get_all_keywords()