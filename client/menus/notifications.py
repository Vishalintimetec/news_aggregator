from client.menus.base import Menu

class NotificationsMenu(Menu):
    def display(self):
        print("\nNotifications Menu:")
        print("1. View Notifications\n2. Configure Notifications\n3. Back")
        choice = input("Choose: ")
        if choice == "1":
            notifications = self.user_api.get_notifications()
            if not notifications:
                print("No notifications found.")
                return
            print(notifications)
            print("\n Notifications:")
            for idx, notif in enumerate(notifications, 1):
                print(f"{idx}. Category: {notif['category'].title()}, Keyword: {notif['keyword']}")
            print(notifications.json())
        elif choice == "2":
            preference_id = input("Enter your notification preference ID: ")
            config = {}
            print("Configure categories (business, entertainment, sports, technology):")
            for cat in ["business", "entertainment", "sports", "technology"]:
                enabled = input(f"Enable {cat}? (y/n): ").lower() == 'y'
                config[cat] = enabled
            keywords = input("Enter keywords (comma separated): ").split(",")
            config["keywords"] = [k.strip() for k in keywords if k.strip()]
            notifications = self.user_api.configure_notifications(preference_id, config)
            print(notifications.json())
        elif choice == "3":
            return
        else:
            print("Invalid choice.")