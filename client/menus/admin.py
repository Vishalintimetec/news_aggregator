from client.menus.base import Menu
from client.menus.hide_unhide import HideUnhideMenu
# from client.menus.block_keyword import BlockKeywordMenu

class AdminMenu(Menu):
    def display(self):
        while True:
            print("\nAdmin Menu:")
            print("1. View list of external servers and status")
            print("2. View external server details")
            print("3. Update/Edit external server details")
            print("4. Add new News Category")
            print("5. Hide/Unhide Articles or Categories")
            print("6. Block/Unblock Keywords")
            print("7. Logout")
            choice = input("Choose: ")
            if choice == "1":
                resp = self.admin_api.get_external_servers()
                print(resp.json())
            elif choice == "2":
                server_id = input("Enter server ID: ")
                resp = self.admin_api.get_external_server_details(server_id)
                print(resp.json())
            elif choice == "3":
                server_id = input("Enter server ID: ")
                api_key = input("Enter new API key: ")
                resp = self.admin_api.update_external_server(server_id, api_key)
                print(resp.json())
            elif choice == "4":
                name = input("Enter new category name: ")
                resp = self.admin_api.add_category(name)
                print(resp.json())
            elif choice == "5":
                HideUnhideMenu(self.user_api, self.admin_api, self.session).display()
            # elif choice == "6":
            #     BlockKeywordMenu(self.user_api, self.admin_api, self.session).display()
            elif choice == "7":
                break
            else:
                print("Invalid choice.")