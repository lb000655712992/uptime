from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# MySql datebase
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@127.0.0.1:3306/db"

db = SQLAlchemy(app)

class config_table(db.Model):
    __tablename__ = 'config_table'
    ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Change = db.Column(db.String(100), nullable=False)
    Threshold = db.Column(db.String(100), nullable=False)
    Duration = db.Column(db.String(100), nullable=False)

    def __init__(self, web_data):
        self.ID = web_data.get("ID")
        self.Change = web_data.get("Change")
        self.Threshold = web_data.get("Threshold")
        self.Duration = web_data.get("Duration")


class data_table(db.Model):
    __tablename__ = 'data_table'
    ID = db.Column(db.Integer, nullable=False, primary_key=True)
    IP = db.Column(db.String(100), nullable=False)
    Hostname = db.Column(db.String(100), nullable=False)
    Username = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    Port = db.Column(db.String(100), nullable=False)
    Uptime = db.Column(db.String(100), nullable=False)
    Status = db.Column(db.String(100), nullable=False)

    def __init__(self, web_data):
        self.ID = web_data.get("ID")
        self.IP = web_data.get("IP")
        self.Hostname = web_data.get("Hostname")
        self.Username = web_data.get("Username")
        self.Password = web_data.get("Password")
        self.Port = web_data.get("Password")
        self.Uptime = web_data.get("Uptime")
        self.Status = web_data.get("Status")


class eMail(db.Model):
    __tablename__ = 'eMail'
    ID = db.Column(db.Integer, nullable=False, primary_key=True)
    eMail = db.Column(db.String(100), nullable=False)

    def __init__(self, web_data):
        self.ID = web_data.get("ID")
        self.eMail = web_data.get("IP")

db.create_all()
