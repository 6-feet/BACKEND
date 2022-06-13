from fastapi import APIRouter, Depends

from core.classes.auth import Authentication


router = APIRouter(
    prefix="/general",
    tags=["general"]
)


@router.get("/")
def greetings_everybody():
    return {"message": "Hi! Happy to see you here"}


@router.get("/protected", dependencies=[Depends(Authentication().requires_authentication)])
def get_protected_information():
    return {"status": "authorized", "message": "Hey hey!"}
