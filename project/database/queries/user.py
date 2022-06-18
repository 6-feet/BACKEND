from sqlalchemy.orm import Session

from database.entities.user import user_models


class UserQuery:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def get_user_by_login(self, database: Session) -> user_models.User | None:
        user = (database.query(user_models.User)
                        .filter(user_models.User.login == self.login)
                        .first())
        return user

    def create_user(self, database: Session) -> user_models.User:
        user = user_models.User(login=self.login, password=self.password)
        database.add(user)
        database.commit()
        database.refresh(user)
        return user
