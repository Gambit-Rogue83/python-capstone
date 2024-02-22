from model import User, db
from server import app

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
