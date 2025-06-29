from datetime import datetime
from client.utils.date_utils import format_datetime

def user_menu(username):
    print(f"\nWelcome to the News Application, {username}!")
    print("Date:", format_datetime(datetime.now(), "date"))
    print("Time:", format_datetime(datetime.now(), "time"))
    print("Please choose the options below:")
    print("1. Headlines")
    print("2. Saved Articles")
    print("3. Search")
    print("4. Notifications")
    print("5. Logout")
    return input("Enter your choice: ")

def headlines_menu():
    print("\nPlease choose the options below for Headlines:")
    print("1. Today")
    print("2. Date range")
    print("3. Logout")
    return input("Enter your choice: ")

def headlines_category_menu():
    print("Please choose the options below for Headlines:")
    print("1. All")
    print("2. Business")
    print("3. Entertainment")
    print("4. Sports")
    print("5. Technology")
    return input("Enter your choice: ")
