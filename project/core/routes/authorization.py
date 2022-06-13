from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.queries.user import UserQuery
from core.classes.auth import Authentication
from core.dependencies import get_database
from core.schemas.auth import AuthDetails, Token


router = APIRouter(
    prefix="/authorization",
    tags=["auth"]
)


@router.post("/signup", response_model=AuthDetails)
def register_user(user: AuthDetails, database: Session = Depends(get_database)):
    auth_handler = Authentication()
    user_instance = UserQuery(user.login, user.password)
    login_exists = user_instance.get_user_by_login(database)
    user_instance.password = auth_handler.get_hashed_password(user_instance.password)
    if login_exists:
        raise HTTPException(status_code=400, detail='The login already exists')
    return user_instance.create_user(database=database)


@router.post("/login", response_model=Token)
def login_user(user: AuthDetails, database: Session = Depends(get_database)):
    auth_handler = Authentication()
    user_instance = UserQuery(user.login, user.password)
    user_from_database = user_instance.get_user_by_login(database=database)
    if user_from_database is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    verified_password = auth_handler.verify_password(user_instance.password, user_from_database.password)
    if not verified_password:
        raise HTTPException(status_code=401, detail="Invalid login or password")
    access_token = auth_handler.create_access_token(user.login)
    return {"access_token": access_token, "token_type": "bearer"}
