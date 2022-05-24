import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Breed(Base):
    __tablename__ = "breed"

    id: UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    breed: str = Column(String(120))
