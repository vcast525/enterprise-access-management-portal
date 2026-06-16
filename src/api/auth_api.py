from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.auth.jwt_utils import (
    create_access_token,
    decode_access_token,
)
from src.auth.password_utils import hash_password
from src.services.user_service import (
    login_user,
    register_user,
)


app = FastAPI()


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    role: str = "User"


class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/")
def root():
    return {
        "message": "Enterprise Access Management Portal API"
    }


@app.post("/register")
def register(request: RegisterRequest):
    hashed_password = hash_password(
        request.password
    )

    user = register_user(
        username=request.username,
        email=request.email,
        password=hashed_password,
        role=request.role,
    )

    return {
        "user_id": user.user_id,
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "is_active": user.is_active,
    }


@app.post("/login")
def login(request: LoginRequest):
    user = login_user(
        username=request.username,
        password=request.password,
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    token = create_access_token(
        username=user.username,
        role=user.role,
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


@app.get("/protected")
def protected(token: str):
    payload = decode_access_token(
        token
    )

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )

    return {
        "message": "Protected access granted",
        "user": payload.get("sub"),
        "role": payload.get("role"),
    }