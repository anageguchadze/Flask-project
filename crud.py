from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///students.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    subject = db.Column(db.String(120), nullable=False)

    
with app.app_context():
    db.create_all()

@app.route("/students", methods=['POST'])
def create_students():
    data = request.get_json()
    new_student = Student(name=data['name'], subject=data["subject"])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student was created!"}), 201

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name, "subject": student.subject} for student in students])


@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student = Student.query.get(id)
    if not student:
        return jsonify({"message": "Student not found"}), 404
    student.name = data['name']
    student.subject = data['subject']
    db.session.commit()
    return jsonify({"message": "Student updated successfully"})


@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"message": "Student not found"}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"})


if __name__=="__main__":
    app.run(debug=True)