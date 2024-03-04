from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(256))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship("User", backref ="games")

class Move(db.Model):
    __tablename__ = 'moves'
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    round_number = db.Column(db.Integer, nullable=False)
    user_movement = db.Column(db.String(25))
    opponent1_move = db.Column(db.String(25))
    opponent2_move = db.Column(db.String(25))

    game = db.relationship("Game", backref="moves")


# class Hunter(db.Model):
#     def __init__(self, movement):
#         self.movement = movement

#     def sniper_shot(self):
#         return "Facing North"

#     def control_relay(self, car):
#         return car

#     def remote_sensor(self):
#         return "Detected"



def connect_to_db(flask_app, db_uri="postgresql:///specter", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    with flask_app.app_context():
        # db.drop_all() # if we don't want to drop the tables remove this
        db.create_all()

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
