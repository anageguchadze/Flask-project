from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.secret_key = 'Secret'

class SimpleForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SimpleForm()
    if form.validate_on_submit():
        return f'Hello {form.name.data}'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run()