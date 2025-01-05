# Flask-project

A simple Flask-based application that demonstrates CRUD (Create, Read, Update, Delete) operations with a RESTful API and a basic HTML form for user interaction.

## Features

- **Frontend**: A simple HTML form for user input.
- **Backend**:
  - Create (POST) functionality for adding new records to the database.
  - Planned functionality: Read (GET), Update (PUT), and Delete (DELETE) operations for full CRUD support.
- **Database**: SQLite database managed with SQLAlchemy.

## Installation

1. Clone the repository:
   git clone https://github.com/anageguchadze/Flask-project.git
   cd Flask-project

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the required dependencies:
pip install -r requirements.txt

Run the application:
python app.py
Access the application in your browser at http://127.0.0.1:5000.

API Endpoints
POST /student
Description: Create a new student record.
Request Body:
json
Copy code
{
    "name": "John Doe",
    "subject": "Mathematics"
}
Response:
json
Copy code
{
    "message": "Student was created!"
}

Planned Endpoints
GET /student/<id>: Retrieve a student's details by ID.
PUT /student/<id>: Update an existing student's details.
DELETE /student/<id>: Delete a student record.

Project Structure
Flask-project/
├── static/
│   └── style.css              # CSS for the form styling
├── templates/
│   └── form.html              # HTML form for user interaction
├── app.py                     # Main Flask application
├── students.db                # SQLite database
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
Future Enhancements
Add full CRUD operations (Read, Update, Delete).
Implement user authentication and authorization.
Improve the frontend with advanced styling or a JavaScript framework.

License
This project is licensed under the MIT License. See the LICENSE file for details.

