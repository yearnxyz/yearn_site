import os,sys
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.web import FallbackHandler, RequestHandler, Application,StaticFileHandler
from tornado.ioloop import IOLoop


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


# 使用shell指令时下面的变量可以在终端中使用，不用再一个个的导入
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# 在 windows 下使用 git 软件自带的terminal可以使用flask shell等指令
# 使用 cmder 是无法使用对应指令的
# 需要在 terminal 中导入的变量有： FLASK_APP=...、FLASK_DEBUG=1

if __name__ == '__main__':
    # create_all只会创建数据库中不存在的表
    # 如果要创建同名新表，最简单的方法是使用 drop_all() 方法删除所有表再创建
    db.app = app
    db.create_all()
    #使用tornado包裹flask app
    tornado_wraped = WSGIContainer(app)
    #设置tornado环境，例如静态文件的路径
    application = Application([(r".*", FallbackHandler, dict(fallback=tornado_wraped)),], static_path = "./app/static") 
    #启动程序
    application.listen(80)
    IOLoop.instance().start()
