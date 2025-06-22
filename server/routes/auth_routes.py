from fastapi import APIRouter, HTTPException

from server.schemas.auth import TokenResponse
from server.schemas.user import UserCreate, UserLogin, UserOut
from server.controller.auth_controller import AuthenticationController

router = APIRouter(prefix="/users", tags=["users"])
auth_controller = AuthenticationController()

@router.post("/register", response_model= UserOut)
def register_user(user: UserCreate):
    return auth_controller.register(user)

@router.post("/login", response_model = TokenResponse)
def login_user(user: UserLogin):
    return auth_controller.login(user)
