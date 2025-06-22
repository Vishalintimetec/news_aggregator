from clients.api.api import AuthAPI
from clients.api.news_api import NewsAPI
from clients.auth import login, signup
from clients.menus.main_menu import main_menu
from clients.menus.user_menu import user_menu, headlines_menu, headlines_category_menu
from clients.menus.admin_menu import admin_menu

def main():
    auth_api = AuthAPI()
    while True:
        choice = main_menu()
        if choice == "1":
            if login(auth_api):
                break
        elif choice == "2":
            signup(auth_api)
        elif choice == "3":
            print("Exiting application.")
            return
        else:
            print("Invalid choice.")

    news_api = NewsAPI(auth_api.token, auth_api.user_id)

    if auth_api.user_role == "admin":
        handle_admin_flow(news_api, auth_api.email)
    else:
        handle_user_flow(news_api, auth_api.email)

def handle_user_flow(api: NewsAPI, email: str):
    while True:
        choice = user_menu(email.split('@')[0].capitalize())
        if choice == "1":
            handle_headlines(api)
        elif choice == "2":
            articles = api.get_saved_articles().json()
            print("Saved Articles:", articles)
        elif choice == "3":
            query = input("Enter search term: ")
            articles = api.search_articles(query).json()
            print("Search Results:", articles)
        elif choice == "4":
            print("Feature not implemented yet.")
        elif choice == "5":
            api.logout()
            break
        else:
            print("Invalid choice.")

def handle_headlines(api: NewsAPI):
    choice = headlines_menu()
    if choice == "1":
        articles = api.get_headlines().json()
        print("Today's Headlines:", articles)
    elif choice == "2":
        start = input("Enter start date (YYYY-MM-DD): ")
        end = input("Enter end date (YYYY-MM-DD): ")
        category = headlines_category_menu()
        print(f"Fetching articles from {start} to {end} in category {category}")
    elif choice == "3":
        api.logout()

def handle_admin_flow(api: NewsAPI, email: str):
    while True:
        choice = admin_menu(email.split('@')[0].capitalize())
        if choice == "1":
            print("All users - (Fetch from backend)")
        elif choice == "2":
            print("API status - (Check APIs)")
        elif choice == "3":
            api.logout()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
