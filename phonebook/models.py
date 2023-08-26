import datetime
from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import relationship, backref
from .database import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, )
    last_name = Column(String, )
    nick_name = Column(String, nullable=True)
    created = Column(DateTime, default=datetime.datetime.now)

    def to_dict(self):
        ignore = ['id', 'created']
        return {col.name: getattr(self, col.name) for col in self.__table__.columns if col.name not in ignore}


class Number(Base):
    __tablename__ = 'numbers'
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, default="phone")
    phone = Column(String, unique=True)
    is_default = Column(Boolean, default=False)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    # set lazy='dynamic' to be abel to query on relationship
    contact = relationship("Contact", backref=backref('numbers', lazy='dynamic'))

    def to_dict(self):
        ignore = ['id', 'contact_id']
        return {col.name: getattr(self, col.name) for col in self.__table__.columns if col.name not in ignore}
