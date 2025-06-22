# from fastapi import Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from server.utils.jwt_utils import decode_token
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
#
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     payload = decode_token(token)
#     if payload is None:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")
#     return payload["sub"]  # usually user_id
