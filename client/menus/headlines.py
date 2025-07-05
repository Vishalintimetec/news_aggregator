from client.menus.base import Menu
from client.utils import input_date

class HeadlinesMenu(Menu):
    def display(self):
        print("\nHeadlines Menu:")
        print("1. Today\n2. Date range\n3. Back")
        choice = input("Choose: ")
        if choice == "1":
            self.show_today_headlines()
        elif choice == "2":
            self.show_date_range_headlines()
        elif choice == "3":
            return
        else:
            print("Invalid choice.")

    def show_today_headlines(self):
        # print("1. All\n2. Business\n3. Entertainment\n4. Sports\n5. Technology")
        # cat_choice = input("Choose category: ")
        # categories = {"1": None, "2": "business", "3": "entertainment", "4": "sports", "5": "technology"}
        # category = categories.get(cat_choice)
        resp = self.user_api.get_headlines_today()
        self.articles_action_menu(resp)

    def show_date_range_headlines(self):
        start = input_date("Enter start date (YYYY-MM-DD): ")
        end = input_date("Enter end date (YYYY-MM-DD): ")
        print("1. All\n2. Business\n3. Entertainment\n4. Sports\n5. Technology")
        cat_choice = input("Choose category: ")
        categories = {"1": None, "2": "business", "3": "entertainment", "4": "sports", "5": "technology"}
        category = categories.get(cat_choice)
        resp = self.user_api.get_headlines_by_date_range(
            start_date=start.isoformat(),
            end_date=end.isoformat(),
            category=category
        )
        self.articles_action_menu(resp)

    def articles_action_menu(self, resp):
        # Print articles
        data = resp.json()
        if isinstance(data, list):
            articles = data
        elif isinstance(data, dict) and "articles" in data:
            articles = data["articles"]
        else:
            articles = []
        if not articles:
            print("No articles found for the selected criteria.")
        else:
            for art in articles:
                print(f"\nArticle Id: {art.get('article_id', art.get('id'))}")
                print(f"Title: {art.get('title')}")
                print(f"Description: {art.get('description')}")
                print(f"Content: {art.get('content')}")
                print(f"Source: {art.get('source')}")
                print(f"URL: {art.get('url')}")
                print(f"Published At: {art.get('published_at')}")
                print(f"Category: {art.get('category', 'N/A')}")
        # Now show the actions menu
        while True:
            print("\nHEADLINES ACTIONS")
            print("1. Back")
            print("2. Logout")
            print("3. Save Article")
            print("4. Like Article")
            print("5. Dislike Article")
            print("6. Mark as Read")
            action = input("Choose: ")
            if action == "1":
                return  # Go back to previous menu
            elif action == "2":
                exit()
            elif action == "3":
                article_id = input("Enter Article ID to save: ")
                save_resp = self.user_api.save_article(article_id)
                print(save_resp.json())
            elif action == "4":
                article_id = input("Enter Article ID to like: ")
                resp = self.user_api.like_article(article_id)
                print(resp.json())
            elif action == "5":
                article_id = input("Enter Article ID to dislike: ")
                resp = self.user_api.dislike_article(article_id)
                print(resp.json())
            elif action == "6":
                article_id = input("Enter Article ID to mark as read: ")
                resp = self.user_api.record_read(article_id)
                print(resp.json())
            else:
                print("Invalid choice.")