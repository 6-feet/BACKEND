import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from database.entities.base import Base


class User(Base):
    __tablename__ = "user"

    id: UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    login: str = Column(String(120), unique=True)
    password: str = Column(String(120))
