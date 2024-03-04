from model import User, db, Game, Move
from server import app
from werkzeug.security import check_password_hash

def create_user(email, username, password):
    user = User.query.filter_by(email=email).first()
    if user:
        return False
    else:
        user = User(email, username, password)

        # with app.app_context():
        db.session.add(user)
        db.session.commit()
        return True

def create_game(user):
    user = User.query.filter_by(username=user).first()
    game = Game()
    db.session.add(game)
    db.session.commit()
    return game.id

def verify_user(username, password):
    user = User.query.filter_by(username=username).first()
    return check_password_hash(user.password_hash, password)
# def user_movement(agentSpace):
