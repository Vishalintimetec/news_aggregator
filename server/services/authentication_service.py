from server.repos.user_repository import UserRepository
from server.schemas.auth import UserCredentials
from server.schemas.user import UserCreate
from server.utils.password_utils import verify_password, hash_password
from server.utils.jwt_utils import create_token
from fastapi import status

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def register_user(self, user: UserCreate):
        if self.user_repo.get_by_email(user.email):
            raise ValueError("Email already registered")
        return self.user_repo.create(user)


    def login(self, user_data: UserCredentials):
        user = self.get_user_by_email(user_data.email)
        if(verify_password(plain_password= user_data.password,
                           hashed_password= user['password'])):
           status = "User Logged in Successfully"
           token_payload = {
               "sub": user["email"],
               "user_id": user["user_id"],
               "role": user["user_role"]
           }
           access_token = create_token(token_payload)

        else:
            raise ValueError("Incorrect Password")
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_role": user["user_role"]
        }


    def get_user_by_email(self, email: str):
        user = self.user_repo.get_by_email(email)
        if user is None:
            raise ValueError("Invalid Email")
        return user