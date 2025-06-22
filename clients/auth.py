from client.api.api import APIClient


def signup(api: APIClient):
    print("\n--- Sign Up ---")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")

    try:
        resp = api.register(username, email, password)
        if resp.ok:
            print(" Registration successful! Please log in.")
        else:
            print(f"Registration failed: {resp.json().get('detail', resp.text)}")
    except Exception as e:
        print(f" Error: {e}")


def login(api: APIClient):
    print("\n--- Login ---")
    email = input("Email: ")
    password = input("Password: ")

    try:
        resp = api.login(email, password)
        if resp.ok:
            print("Login successful!")
            return True
        else:
            print(f"Login failed: {resp.json().get('detail', resp.text)}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False
