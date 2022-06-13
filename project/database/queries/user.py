from sqlalchemy.orm import Session

from database.entities.user.user_models import User


class UserQuery:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def get_user_by_login(self, database: Session) -> User | None:
        user = database.query(User).filter(User.login == self.login).first()
        return user

    def create_user(self, database: Session) -> User:
        user = User(login=self.login, password=self.password)
        database.add(user)
        database.commit()
        database.refresh(user)
        return user
