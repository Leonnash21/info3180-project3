from flasApp import db 
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy.schema import ForeignKey


 
#  db = SQLAlchemy()


class Users(db.Model):     
    id = db.Column(db.Integer, primary_key=True)    
    username = db.Column(db.String(80)) 
    firstname = db.Column(db.String(80))     
    lastname = db.Column(db.String(80)) 
    sex = db.Column(db.String(50)) 
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(54)) 
    image= db.Column(db.LargeBinary) 
 
    query = db.Query("Users")
    
    def __init__(self, username, firstname, lastname, sex, email, password, image):
        
        self.username=username
        self.firstname=firstname.title()
        self.lastname=lastname.title()
        self.sex = sex.upper()
        self.email=email.lower()
        self.password = password
        self.image=image
        
        
    def set_password(self, password):
        self.password = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.password, password)
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    # def get_id(self):
    #     try:
    #         return unicode(self.id)  # python 2 support
    #     except NameError:
    #         return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.firstname)
        
        
class wishList(db.Model):
    #__tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    owner = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    
    query = db.Query("wishList")

    def __init__(self, title, owner):
        
        self.title = title
        self.owner = owner

    def __repr__(self):
        return "Wishlist {}".format(self.title)
    
    


class WishL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String, index=True)
    url = db.Column(db.String, index=True)
    list_id = db.Column(db.Integer, ForeignKey('wish_list.id'), nullable=False)


    query = db.Query("WishL")
    def __init__(self, owner, title, description, url, list_id):
        
        self.title = title
        self.description = description
        self.url = url
        self.owner = owner
        self.list_id = list_id

    def __repr__(self):
        return 'Wish {}'.format(self.title)