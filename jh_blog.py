import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment

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
    app.run(debug=True,host='0.0.0.0',port=80)