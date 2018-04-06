from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


#display form
@app.route('/')
def display_signup_form():
    return render_template('signup_form.html')

#error validation functions
def empty_field(x):
    if x:
        return True
    else:
        return False

def input_length(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

def at_symbol(x):
    if x.count('@') >= 1:
        return True
    else:
        return False

def multiple_at_symbols(x):
    if x.count('@') <= 1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.') >= 1:
        return True
    else:
        return False

def multiple_email_periods(x):
    if x.count('.') <= 1:
        return True
    else:
        return False

#process validations
@app.route('/', methods=['POST'])
def validate_info():
    user_name = request.form['user_name']
    email_address = request.form['email_address']
    user_password = request.form['user_password']
    password_verify = request.form['password_verify']
    
    username_error = ''
    email_error = ''
    password_error = ''
    password_verify_error = ''
 
    required_error = 'This field is required'
    reenter_password = 'Please re-enter password'
    input_length_error = 'Must be between 3 and 20 characters'
    spaces_error = 'Must not contain spaces'

    #username validation conditions
    if not empty_field(user_name):
        username_error = required_error
        password_error = reenter_password
        password_verify_error = reenter_password

    elif not input_length(user_name):
        username_error = input_length_error
        password_error = reenter_password
        password_verify = reenter_password

    else:
        if " " in user_name:
            username_error = spaces_error
            password_error = reenter_password
            password_verify_error = reenter_password

    #user_password validation conditions
    if not empty_field(user_password):
        password_error = required_error

    elif not input_length(user_password):
        password_error = input_length_error
        password_verify_error = reenter_password
    
    else:
        if " " in user_password:
            password_error = spaces_error
            password_verify_error = reenter_password
    
    if not empty_field(password_verify):
        password_verify_error = required_error

    else:
        if user_password != password_verify:
            password_verify_error = 'Passwords must match'
            password_error = 'Passwords must match'

    #email validation conditions
    if empty_field(email_address):
        if not input_length(email_address):
            email_error = input_length_error
            user_password = ''
            password_verify = ''
            password_error = reenter_password
            password_verify_error = reenter_password
        elif not at_symbol(email_address):
            email_error = "Email must contain the @ symbol"
            user_password = ''
            password_verify = ''
            password_error = reenter_password
            password_verify_error = reenter_password
        elif not multiple_at_symbols(email_address):
            email_error = "Email must contain only one @ symbol"
            user_password = ''
            password_verify = ''
            password_error = reenter_password
            password_verify_error = reenter_password
        elif not email_period(email_address):
            email_error = "Email must contain ."
            user_password = ''
            password_verify = ''
            password_error = reenter_password
            password_verify_error = reenter_password
        elif not multiple_email_periods(email_address):
            email_error = "Email must contain only one ."
            user_password = ''
            password_verify = ''
            password_error = reenter_password
            password_verify_error = reenter_password
        else:
            if " " in email_address:
                email_error = spaces_error
                user_password = ''
                password_verify = ''
                password_error = reenter_password
                password_verify_error = reenter_password

    if not username_error and not password_error and not password_verify_error and not email_error:
        user_name = user_name
        return redirect('/welcome?user_name={0}'.format(user_name))
    
    else:
        return render_template('signup_form.html', user_name=user_name, username_error=username_error, user_password=user_password,
        password_error=password_error, password_verify=password_verify, password_verify_error=password_verify_error, 
        email_address=email_address, email_error=email_error)

@app.route('/welcome')
def welcome():
    user_name = request.args.get('user_name')
    return render_template('welcome.html', user_name=user_name)


app.run()