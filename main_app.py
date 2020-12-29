import app
from flask_login import login_user, logout_user, login_required
from flask import request
import layoutAnalyse

from pdfminer.pdfparser import  PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

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

@App.route('/shelf/uploadIMG', methods=['GET', 'POST'])
@login_required
def uploadIMG():
    '''
    用户通过上传图片方式上传资料
    '''
    msg =  None
    if request.method == 'POST':
        # 获取图像列表
        imgs = request.form.get('img')
        # 处理图片
        msg = getMessageFromIMG(imgs)
    return msg

def getMessageFromIMG(imgs):
    # analyse = layoutAnalyse()
    # for img in imgs:
    #     # 获取板块分析后的图片列表
    #     new_imgs = analyse.analyse()
    #     # 循环，接入接口，获得文本信息
    return message

@App.route('/shelf/uploadPDF', methods=['GET', 'POST'])
@login_required
def uploadPDF():
    msgs = None
    if request.method == 'POST':
        # 获取文件
        pdf_file = request.form.get('pdf_file')
        # 处理文件
        msgs = getMessageFromPDF(pdf_file)
        # 处理获得的文本信息
    return msgs

def getMessageFromPDF(pdf_file):
    '''
    解析PDF文本
    '''
    # 创建PDF文档分析器
    parser = PDFParser(pdf_file)
    # 创建PDF文档
    doc = PDFDocument()
    # 链接分析器，与文档对象
    parser.set_document(doc)
    doc.set_parser

    doc.initialize()
    msgs = None
    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDF资源管理器，来共享资源
        manager = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(manager, laparams=laparams)
        # 创建一个PDF解释其对象
        interpreter = PDFPageInterpreter(manager, device)

        # doc.get_pages() 获取page列表
        for page in doc.get_pages():
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # LTPage对象 里面存放着 这个page解析出的各种对象
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal
            for x in layout:
                # 对不同对象做不同转换
                # 对于图片
                if(isinstance(x, LTImage)):
                    # msg = getMessageFromIMG(x)
                    break
    return msgs

#笔记搜索接口
@App.route('/note/search', methods=['GET', 'POST'])
@login_required
def noteSearch():
    '''
    content: 传入参数，用户键入搜索内容
    notelist: 传入参数，笔记信息列表
    notelist[i]: 字典，笔记信息
    '''
    notelist = None
    if request.method == "GET":
        content = request.args.get("content")

        # 根据用户键入的搜索内容，查询数据库中与之匹配的用户的全部笔记
        # notelist = getNoteList(content)
    return notelist

#获取笔记总列表接口
@App.route('/note/All', methods=['GET', 'POST'])
@login_required
def noteAll():
    '''
    content: 传入参数，用户键入搜索内容
    booklist: 传入参数，书籍信息列表
    booklist[i]: 字典，书籍信息
    '''
    notelist = None
    if request.method == "GET":
        content = request.args.get("content")

        # 根据获取到的响应查询相应用户的数据库，查询该用户所做笔记的全部书籍与信息
        # booklist = getBookList(content)
    return booklist

#获取单本笔记子目录接口
@App.route('note/anote', methods=['GET', 'POST'])
@login_required
def noteAnote():
    '''
    content: 传入参数，用户键入搜索内容
    notelist: 传入参数，笔记信息列表
    notelist[i]: 字典，笔记信息
    '''
    notelist = None
    if request.method == "GET":
        content = request.args.get("content")

        # 根据获取到的响应查询响应用户书籍的数据库，查询该用户该本书的全部笔记信息
        # notelist = getNoteList(content)
    return notelist

if __name__ == '__main__':
    App.run(debug=True, host='127.0.0.1', port='8888')