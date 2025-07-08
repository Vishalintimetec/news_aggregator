from client.menus.base import Menu

class BlockKeywordMenu(Menu):
    def display(self):
        print("\nBlock/Unblock Keyword Menu:")
        print("1. Block Keyword")
        print("2. Unblock Keyword")
        print("3. Back")
        choice = input("Choose: ")
        if choice == "1":
            keyword = input("Enter keyword to block: ")
            resp = self.admin_api.block_keyword(keyword)
            print(resp.json())
        elif choice == "2":
            keyword = input("Enter keyword to unblock: ")
            resp = self.admin_api.unblock_keyword(keyword)
            print(resp.json())
        elif choice == "3":
            return
        else:
            print("Invalid choice.")