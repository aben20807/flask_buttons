from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = False
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

valid_key = ['u', 'i', 'o',
             'j', 'k', 'l',
             'm', ',', '.',
             'q', 'w', 'e',
             'z', 'x', 'c']

@app.route("/", methods=['GET', 'POST'])
def contact():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        get_key = request.form['submit']
        if  get_key in valid_key:
            web_key = get_key
            printcolor(get_key)
        else:
            web_key = ''
            printcolor("?")
    return render_template('index.html', form=form)

def printcolor(s):
    print "\033[1;31mkey = " + s + "\033[m"

if __name__ == "__main__":
    global web_key
    app.run()
