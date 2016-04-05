from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = "this is a super secure key"
# app.config['OPENID_PROVIDERS'] = COMMON_PROVIDERS

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:newp@localhost/name"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://yzicurmnvkqqhp:Kpl-6hLvDaRcPCelsrxdmydSgi@ec2-23-21-219-209.compute-1.amazonaws.com:5432/de7vj5i2j9deb1"
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
# oid = OpenID(app,'/tmp')

from flasApp import views, models
from flasApp.models import Users, wishList, WishL