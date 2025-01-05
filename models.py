from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"
    
with app.app_context():
    db.create_all()

@app.route("/add_user")
def add_user():
    new_user = User(name="John Doe", email="johnatan@gmail.com")
    db.session.add(new_user)
    db.session.commit()
    return f"User {new_user.name} added"

if __name__=="__main__":
    app.run(debug=True)