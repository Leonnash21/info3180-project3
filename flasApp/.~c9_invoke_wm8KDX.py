"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from flasApp import app, db
from flask import render_template, request, redirect, url_for,jsonify,g,session
import flasApp
# from models import db
from flask.ext.wtf import Form 
from wtforms.fields import TextField, PasswordField 
from wtforms.validators import Required, Email
import os
from werkzeug import secure_filename

from models import Users, wishList
import requests
import BeautifulSoup
import urlparse

from flask import render_template, request, redirect, url_for, Flask, flash, jsonify

from flask.ext.login import login_user, logout_user, current_user, login_required
from flasApp import app, lm
from flask.ext.login import LoginManager
import forms
from forms import SignupForm, LoginForm, wishListForm

import random
from random import randrange, randint
import flask_login
  
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)

@app.before_request
def before_request():
    g.user = current_user
    
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    
    
    
    
    

                      

@app.route('/signup/', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        id = random.randint(1000000, 1099999)
        username =request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        sex = request.form['sex']
        email = request.form['email']
        password = request.form['password']

        
        file = request.files['image']
        image = secure_filename(file.filename)
        file.save(os.path.join("pics", image))

        # write the information to the database
        newuser = Users(id, username, firstname, lastname, sex, email, password, image)
        db.session.add(newuser)
        db.session.commit()
        
        
        flash ('User' + username + 'sucessfully added!')

        return "{} {} was added to the database".format(request.form['firstname'],
                                             request.form['lastname'])

    form = SignupForm()
    return render_template('signup.html',
                           form=form)
                           


# @app.route('/login', methods=['GET', 'POST'])
# @lm.request_loader
# def load_user(request):
#     token = request.headers.get('Authorization')
#     if token is None:
#         token = request.args.get('token')

#     if token is not None:
#         username,password = token.split(":") # naive token
#         user = Users.get(username)
#         if (user is not None):
#             user = Users(Users[0],Users[1])
#             if (user.password == password):
#                 return user
#     return None                    




@app.route('/login/', methods=['GET', 'POST'])
def login():
    
    # all_users = db.session.query(Users).current_user()
  
    
    # if current_user in all_users:
        
    #     return redirect(Url for('WishList'))
        
    
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('WishList'))
    form = LoginForm()
    
    
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        username = request.form['username']
        password = request.form['password']
        # Login and validate the user.
        # user should be an instance of your `Users` class
        user = Users.query.filter_by(username=username, password=password).first()
        
        
        user = load_user("1")
        login_user(user)
        
        flash("Logged in successfully.")
        
        return redirect(request.args.get("next") or url_for("WishL"))
    
        
    form = LoginForm()
    return render_template('login.html', form=form)
    
                           
       
# @app.route('/login', methods=['GET', 'POST'])
# @lm.request_loader
# def login():
    
#     form = LoginForm()
#     if form.validate_on_submit():
       
#         login_user(user)

#         flask.flash('Logged in successfully.')

#         next = flask.request.args.get('next')
#         # next_is_valid should check if the user has valid
#         # permission to access the `next` url
#         if not next_is_valid(next):
#             return flask.abort(400)

#         return flask.redirect(next or flask.url_for('index'))
#     return flask.render_template('login.html', form=form)  
   
    

@app.route("/wishlist/", methods=['GET', 'POST'])
def WishL():
    
    if request.method == 'POST':
        url = request.form['url']
        itemName = request.form['itemName']
        
        
        # result = requests.get(url)
        # soup = BeautifulSoup.BeautifulSoup(result.text)
        # og_image = (soup.find('meta', property='og:image') or soup.find('meta', attrs={'name': 'og:image'}))
     
        # write the information to the database
        newlist = wishList(url=url, itemName=itemName)
        db.session.add(newlist)
        db.session.commit()
        
        
        flash ('List' + itemName + 'sucessfully added!')

        return "{} {} was added to the database".format(request.form['url'], request.form['itemName'])

    form = wishListForm()
    return render_template('wishList.html',
                           form=form)
     
    #  imageList = list()
    #  image = """<img src="%s"><br />"""
    #  for img in soup.findAll("img", src=True):
    #     if "sprite" not in img["src"]:
    #         if request.headers['Content-Type']=='application/json' or request.method == 'POST':
    #             imageList.append(image % urlparse.urljoin(url, img["src"]))
    #             return jsonify(imageList)
            
    #         thumbnail_spec = soup.find('link', rel='image_src')
            
    #         if thumbnail_spec and thumbnail_spec['href']:
    #             imageList.append(image % urlparse.urljoin(url, img["src"]))
                
                    
    #                 return "{} {} was added to the database".format(request.form['url'], request.form['itemName'])
    #     form = wishListForm()                    
    #     return render_template('wishList.html', form=form)
                            
                            
        
# @app.route('/images/', methods = ['GET', 'POST'])
# @login_required
# # def image_dem():

@app.route('/wishlists/', methods=['GET', 'POST'])
def wish():
    # list = wishList.query.all()
    all_users = db.session.query(wishList).all()
    users = []
    result = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(result.text)
    og_image = (soup.find('meta', property='og:image') or
                    soup.find('meta', attrs={'name': 'og:image'}))
    if og_image and og_image['content']:
        return og_image['content']

    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        return thumbnail_spec['href']
        
    for user in all_users:
        users.append({"id": user.id, "url":user.url, "itemName":user.itemName})
    if request.headers['Content-Type']=='application/json' or request.method == 'POST':
        return jsonify(users=users)
    return render_template('wishlists.html', users=users)
    
@app.route('/wishlist/<int:id>/')
def view_list(id):
    users= db.session.query(wishList).filter_by(id=id).first() 
    return render_template('view_list.html', wishlist=users)
    
@app.route("/logout")
@login_required
def logout():
    form = LoginForm()
    logout_user()
    return redirect('login.html', form=form)
    
    
    
    
    
    
@app.route('/profiles/',methods=["POST","GET"])
def profile_list():
    profiles = Users.query.all()
    if request.method == "POST":
        return jsonify({"age":4, "name":"John"})
    return render_template('profile_list.html',
                            profiles=profiles)

@app.route('/profile/<int:id>')
def profile_view(id):
    profile = Myprofile.query.get(id)
    return render_template('profile_view.html',profile=profile)


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
