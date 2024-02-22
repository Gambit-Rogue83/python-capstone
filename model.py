from flask_sqlalchemy import SQLAlchemy
# from server import app
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_migrate import Migrate
db = SQLAlchemy()
# Migrate(app, db)



# login_manager = LoginManager()

# login_manager.init_app(app)
# login_manager.login_view = 'login'

# die_sides = ["1", "2", "3", "4", "5", "6"]

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

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




def connect_to_db(flask_app, db_uri="postgresql:///specter", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    with flask_app.app_context():
        db.drop_all() # if we don't want to drop the tables remove this
        db.create_all()

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
