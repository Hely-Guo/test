import app
from flask_login import login_user, logout_user, login_required

App = app.app
login = app.login

@login.user_loader
def load_user(user_id):
    """
        user_loader回调：
        用于从会话中存储的用户ID重新加载用户对象
    """
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
    """
        用户登陆处理
    """
    return 'login'

@App.route('/logout')
def logout():
    """
        用户登出处理
    """
    logout_user()

@App.route('/')
@login_required
def main_page():
    return 'Jackson Wang'


if __name__ == '__main__':
    App.run(debug=True, host='127.0.0.1', port='8888')