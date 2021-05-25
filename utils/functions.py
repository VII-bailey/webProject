import os

import redis
from flask import Flask
from App.models import db


def create_app():
    # 定义系统路径的变量
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # 定义静态文件的路径
    static_dir = os.path.join(BASE_DIR, 'static')

    # 定义模板文件的路径
    templates_dir = os.path.join(BASE_DIR, 'templates')

    # 初始化 app 和 manage.py 文件关联
    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir)

    # 注册蓝图
    app.register_blueprint(url_prefix='/user')

    # 配置 mysql 数据库
    app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+pymysql://root:148103@192.168.58.128:3306/web'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 设置 session 密钥
    app.config['SECRET_KEY'] = 'secret_key'

    # 设置连接的 redis 数据库，默认连接到本地 6379
    app.config['SESSION_TYPE'] = 'redis'

    # 设置远程
    app.config['SESSION_REDIS'] = redis.Redis(host=None, port=None)

    # 初始化 db
    db.init_app(app=app)

    return app
