import app
from flask_login import login_user, logout_user, login_required

App = app.app
login = app.login

@login.user_loader
def load_user(user_id):
    user = {
        'id': 1,
        'name': 'Jackson Wang',
        'pwd': '1234567'
    }
    if(user_id == 1):
        return user
    return None

@App.route('/login')
def login():
    return 'login'


@App.route('/')
@login_required
def hello_world():
    return 'Jackson Wang'

@App.route('/logout')
def logout():
    logout_user()

if __name__ == '__main__':
    App.run(debug=True, host='127.0.0.1', port='8888')