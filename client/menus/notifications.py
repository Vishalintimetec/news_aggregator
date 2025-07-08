from client.menus.base import Menu

class NotificationsMenu(Menu):
    def display(self):
        print("\nNotifications Menu:")
        print("1. View Notifications\n2. Configure Notifications\n3. Back")
        choice = input("Choose: ")
        if choice == "1":
            resp = self.user_api.get_notifications()
            print(resp.json())
        elif choice == "2":
            preference_id = input("Enter your notification preference ID: ")
            config = {}
            print("Configure categories (business, entertainment, sports, technology):")
            for cat in ["business", "entertainment", "sports", "technology"]:
                enabled = input(f"Enable {cat}? (y/n): ").lower() == 'y'
                config[cat] = enabled
            keywords = input("Enter keywords (comma separated): ").split(",")
            config["keywords"] = [k.strip() for k in keywords if k.strip()]
            resp = self.user_api.configure_notifications(preference_id, config)
            print(resp.json())
        elif choice == "3":
            return
        else:
            print("Invalid choice.")