from flasApp import db 
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash


 
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
    
    def __init__(self, id, username, firstname, lastname, sex, email, password, image):
        self.id = id
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
    username = db.Column(db.String(80))
    url = db.Column(db.String(500), index=True, unique=True)
    itemName = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    image_url = db.Column(db.String(500))
    
    
    
    query = db.Query("wishList")
    
    def __init__(self, url, itemName,description,image_url,username ):
        self.url = url
        self.itemName = itemName
        self.description = description  
        self.image_url = image_url
        self.username= username
        
    def __repr__(self):
        return '<WishList %r>' % (self.url)
        