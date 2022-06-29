from sqlalchemy.orm import Session

from database.models import user


class UserQuery:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def get_user_by_login(self, database: Session) -> user.User | None:
        current_user = (database.query(user.User)
                        .filter(user.User.login == self.login)
                        .first())
        return current_user

    def create_user(self, database: Session) -> user.User:
        created_user = user.User(login=self.login, password=self.password)
        database.add(created_user)
        database.commit()
        database.refresh(created_user)
        return created_user
