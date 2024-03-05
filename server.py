import os
import crud
from flask import Flask, render_template, request, flash, abort, redirect, url_for, session, jsonify
import model
import logic

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'IAmIRONMAN'

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        user = request.form.get('username')
        password = request.form.get('password')
        if crud.create_user(email, user, password):
            session['user'] = user
            print(session)
            return redirect('session')
        else:
            flash('Account already exists')
            return redirect('login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        if crud.verify_user(user, password):
            session['user'] = user
            flash(f"Welcome back {user}")
            return redirect('session')
        else:
            flash('The email or password you provided does not exist, please try again!')
            return redirect('login')
    return render_template('login.html')

@app.route('/logout')
def logout():
    flash("Logged out successfully")
    return redirect(url_for('login'))

@app.route('/session', methods=['GET', 'POST'])
def new_game():
    if session.get('user'):
        return render_template('session.html')


    return redirect('login')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if not session.get('user'):
        return redirect('/login')

    if not session.get('game.id'):
        session['game.id']  = crud.create_game(session['user'])

    print(session)
    game_spaces = []
    game_letters = 'ABCDEFGHIJKLMNOPQRSTUVW'
    game_numbers = list(range(1,33))

    for num in game_numbers:
        list1 = []
        for letter in game_letters:
            list1.append(letter + str(num))
        game_spaces.append(list1)

    return render_template('game.html', game_spaces=game_spaces)

@app.route('/game-update', methods=['POST'])
def game_update():
    round_number = 1
    agentField = request.json.get("agentField")
    agentDetected = request.json.get("agentDetected")
    taskCompleted =request.json.get('taskCompleted')
    team_moves = logic.opponent(agentField, agentDetected, taskCompleted)

    with app.app_context():
        movement = model.Move(game_id=session['game.id'], round_number= round_number, user_movement =agentField, opponent1_move =team_moves[1], opponent2_move =team_moves[0])
        model.db.session.add(movement)
        model.db.session.commit()
    round_number += 1
    return jsonify(team_moves[0], team_moves[1])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    model.connect_to_db(app)
    app.run(debug = True)
