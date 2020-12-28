import app
from flask_login import login_user, logout_user, login_required
from flask import request

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
    '''
    用户登陆处理
    '''
    return 'login'

@App.route('/logout')
def logout():
    '''
    用户登出处理
    '''
    logout_user()

@App.route('/')
@login_required
def main_page():
    return 'Jackson Wang'

@App.route('/library/public', methods=['GET', 'POST'])
@login_required
def libraryPublic():
    '''
    content: 传入参数，用户键入搜索内容
    booklist: 数组，书本信息列表
    booklist[i]: 字典，书本信息
    '''
    booklist = None
    if request.method == "GET":
        content = request.args.get("content")

        # booklist = getBookList(content)
    return booklist


@App.route('/library/share', methods=['GET', 'POST'])
@login_required
def libraryShare():
    '''
    project_name: 传入参数，创建项目名称
    project_pwd: 传入参数，创建项目密钥
    msg_project: 返回数据，项目信息
    '''
    msg_project = None
    if request.method == "POST":
        project_name = request.form.get("project_name")
        project_pwd = request.form.get("project_pwd")
        project_id = isProject(project_name, project_pwd)
        if project_id:
            msg_project = getProject(project_id)
        
    return msg_project

def isProject(project_name, project_pwd):
    '''
    判断该项目是否已被创建。若被创建，返回项目id；否则返回None
    project_name: 项目名
    project_pwd: 项目密钥
    pid: 项目id
    '''
    pid = None
    # 查找数据库
    p = project.query.filter_by(name=project_name, password=project_pwd).first()
    if p:
        pid = p.id
    return pid

def getProject(project_id):
    '''
    根据项目编号，判断项目是否存在。若存在返回项目信息；否则返回None
    project_id: 项目编号
    pmsg: 项目信息
    '''
    pmsg = project.query.filter_by(id=project_id).first()
    return pmsg


if __name__ == '__main__':
    App.run(debug=True, host='127.0.0.1', port='8888')