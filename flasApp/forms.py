from flask_wtf.file import FileAllowed, FileRequired
from wtforms.validators import DataRequired, Required, Length, Email, EqualTo, url
from wtforms import validators, ValidationError
from wtforms.fields import TextField, FileField, TextAreaField, SelectField, SubmitField, StringField, BooleanField, PasswordField
from models import Users, wishList
from flasApp import db
from flask.ext.wtf import Form
from wtforms.fields.html5 import URLField

class SignupForm(Form):
    
    username = TextField("Username",  [validators.Required("Please enter a username.")])
    firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
    lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    confirm_email = TextField('Confirm Email', validators=[Required(), Email()])
    password = PasswordField("Password", [validators.Required("Please enter a password.")])
    confirm_password = PasswordField('Re-enter Password', validators=[Required()])
    image = FileField('Profile Photo', validators=[FileAllowed(['jpg,png'], 'Images Only!')])
    sex = SelectField('Sex', choices=[('Male', 'Male'), ('Female','Female')], validators=[Required()])
    submit = SubmitField("Create account")
 
    def __init__(self, *args, **kwargs):
      Form.__init__(self, *args, **kwargs)
 
    def validate(self):
      if not Form.validate(self):
        return False
     
      user = Users.query.filter_by(email = self.email.data.lower()).first()
      if user:
         self.email.errors.append("That email is already taken")
         return False
      else:
         return True


class LoginForm(Form):
  
  
    username = TextField("Email",  [validators.Required("Please enter your username."), validators.Email("Please enter your username.")]) 
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField("Login")
    
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        
        
        
        def validate(self):
          if not Form.validate(self):
            return False
            
          user = db.query ("Users")
          if user:
            self.email.append("Welcome")
            return True
          else:
            self.email.errors.append("User does not exist")
            return False
            
            
      

class wishListForm(Form):
  
  title = TextField('Title', validators=[Required()])  # add per user validation
  create = SubmitField('Create')
	
	
	
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
    
    
    def validate(self):
      if not Form.validate(self):
        return False
        
        
        
      wlist = db.query ("wishList")
      if wlist:
        self.email.errors.append("Url already exists")
        return False
      else:
        return True
        
        
        
class WishLForm(Form):
	title = TextField('Title', validators=[Required()]) 
	description = TextAreaField('Description', validators=[Required()]) 
	url = URLField('URL', validators=[url()]) 
	enter = SubmitField('Add') 
	
	def __init__(self, *args, **kwargs):
	  Form.__init__(self, *args, **kwargs)
	  
	  
	  
	def validate(self):
	  if not Form.validate(self):
	    return False
	    
	    
	    
	    
	  wish = db.query ("WishL")
	  if wish:
	    self.email.errors.append("Url already exists")
	    return False
	  else:
	    return True