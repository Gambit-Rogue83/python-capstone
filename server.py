import os
import crud
from flask import Flask, render_template, request, flash, abort, redirect, url_for, session
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
import model

app = Flask(__name__)

app.config['SECRET_KEY'] = 'IAmIRONMAN'

@app.route('/', methods=['GET', 'POST'])
def register():
    # form = GamerTag()
    if request.method == 'POST':
        email = request.form.get('email')
        user = request.form.get('username')
        password = request.form.get('password')
        if crud.create_user(email, user, password):
            session['user'] = user

            return redirect('session')
    #     db.session.add(user)
    #     db.session.commit()
    #     flash(f"{user.username}, let the games begin!")
    #     return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/session')  #/welcome
def new_game(): #welcome_user:

    if not session.get('user'):
        return redirect('/login')


    return render_template('session.html') #welcome_user.html

@app.route('/logout')
def logout():
    # logout_user()
    flash("Logged out successfully")
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():

    # form = LoginForm()
    # if form.validate_on_submit():
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
    model.connect_to_db(app)
    app.run(debug = True)
