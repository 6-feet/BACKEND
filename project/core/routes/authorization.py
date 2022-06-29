from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.queries.user_query import UserQuery
from core.classes.authentication import Authentication
from core.dependencies import get_database
from core.schemas.auth import AuthDetails, Token


router = APIRouter(
    prefix="/authorization",
    tags=["auth"]
)


@router.post("/signup", response_model=AuthDetails)
def register_user(user: AuthDetails, database: Session = Depends(get_database)):
    user_from_db = UserQuery(**user.dict()).get_user_by_login(database)
    if user_from_db:
        raise HTTPException(status_code=400, detail='The login already exists')
    profile = Authentication().create_profile(user.login, user.password, database)
    return profile


@router.post("/login", response_model=Token)
def login_user(user: AuthDetails, database: Session = Depends(get_database)):
    user_from_db = UserQuery(**user.dict()).get_user_by_login(database)
    if user_from_db is None:
        raise HTTPException(
            status_code=404,
            detail="User does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )
    verified_password = Authentication().verify_password(user.password,
                                                         user_from_db.password)
    if not verified_password:
        raise HTTPException(status_code=401, detail="Incorrect login or password")
    access_token = Authentication().create_access_token(user.login)
    return {"access_token": access_token, "token_type": "bearer"}
