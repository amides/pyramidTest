from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

class ContactModel(Base):
    __tablename__ = 'contact_data'

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    last_name = Column(Text, unique=True)
    email = Column(Text, unique=True)
    telephone = Column(Integer)
    address = Column(Text, unique=True)
      


Index('my_index', MyModel.name, unique=True, mysql_length=255)
