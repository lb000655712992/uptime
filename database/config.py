from sqlalchemy import create_engine, Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import datetime


MySQL_user = "root"
MySQL_password = "password"
MySQL_server = "127.0.0.1"
MySQL_port = "3306"
MySQL_database = "db"

sqlite_url = "mysql+pymysql://" +\
    MySQL_user + ":" +\
    MySQL_password + "@" +\
    MySQL_server + ":" +\
    MySQL_port + "/" +\
    MySQL_database

engine = create_engine(sqlite_url)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class config_table(Base):
    __tablename__ = 'config_table'
    ID = Column(Integer, nullable=False, primary_key=True)
    Change = Column(String(100), nullable=False)
    Threshold = Column(String(100), nullable=False)
    Duration = Column(String(100), nullable=False)

    def __init__(self, web_data):
        self.ID = web_data.get("ID")
        self.Change = web_data.get("Change")
        self.Threshold = web_data.get("Threshold")
        self.Duration = web_data.get("Duration")


class data_table(Base):
    __tablename__ = 'data_table'
    ID = Column(Integer, nullable=False, primary_key=True)
    IP = Column(String(100), nullable=False)
    Hostname = Column(String(100), nullable=False)
    Username = Column(String(100), nullable=False)
    Password = Column(String(100), nullable=False)
    Port = Column(String(100), nullable=False)
    Uptime = Column(String(100), nullable=False)
    Status = Column(String(100), nullable=False)

    def __init__(self, web_data):
        self.ID = web_data.get("ID")
        self.IP = web_data.get("IP")
        self.Hostname = web_data.get("Hostname")
        self.Username = web_data.get("Username")
        self.Password = web_data.get("Password")
        self.Port = web_data.get("Port")
        self.Uptime = web_data.get("Uptime")
        self.Status = web_data.get("Status")


class eMail(Base):
    __tablename__ = 'eMail'
    ID = Column(Integer, nullable=False, primary_key=True)
    eMail = Column(String(100), nullable=False)

    def __init__(self, eMail_data):
        self.ID = eMail_data.get("ID")
        self.eMail = eMail_data.get("eMail")


class data_tableSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = data_table
        include_relationships = True
        load_instance = True


class eMailSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = eMail
        include_relationships = True
        load_instance = True


class config_tableSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = config_table
        include_relationships = True
        load_instance = True
