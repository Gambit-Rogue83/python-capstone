import os
from flask import Flask, render_template, request, flash, abort, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# from flask_migrate import Migrate
from flask_login import login_user, login_required, logout_user
from forms import GamerTag, LoginForm
from model import User, db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'IAmIRONMAN'

@app.route('/', methods=['GET', 'POST'])
def register():

    form = GamerTag()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash(f"{user.username}, let the games begin!")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/session')  #/welcome
@login_required
def new_game(): #welcome_user:


    return render_template('session.html') #welcome_user.html

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash(f"Welcome back {user.username}")

            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('session')

            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/game')
@login_required
def game():

    game_spaces = []
    game_letters = 'ABCDEFGHIJKLMNOPQRSTUVW'
    game_numbers = list(range(1,33))

    for num in game_numbers:
        list1 = []
        for letter in game_letters:
            list1.append(letter + str(num))
        game_spaces.append(list1)
    return render_template('game.html', game_spaces=game_spaces)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug =True)
