from server.repos.blocked_keyword_repo import BlockedKeywordRepo

class BlockedKeywordService:
    def __init__(self):
        self.repo = BlockedKeywordRepo()

    def add_keyword(self, keyword):
        return self.repo.add_keyword(keyword)

    def remove_keyword(self, keyword):
        return self.repo.remove_keyword(keyword)

    def get_all_keywords(self):
        return self.repo.get_all_keywords()