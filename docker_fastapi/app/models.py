from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Mock_Data(Base):
    __tablename__ = "MOCK_DATA"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    gender = Column(String)
    ip_address = Column(String)
    city = Column(String)
    guid = Column(String)

