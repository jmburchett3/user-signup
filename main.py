from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def display_signup_form():
    return render_template('signup_form.html')

@app.route('/', methods=['POST'])
def validate_info():
    username_error = ''
    user_name = request.form['user_name']
    if user_name == '':
        username_error = 'Please add a valid username'
        return render_template('signup_form.html', username_error=username_error)

    else:
        user_name = request.form['user_name']
        return redirect('/welcome')

@app.route('/welcome', methods=['POST'])
def welcome():
    user_name = request.form['user_name']
    return render_template('welcome.html', user_name=user_name)


app.run()