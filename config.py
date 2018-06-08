import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '28#oN^^VfhcxV7x8H32yGOGIk2wLY%OFi!!V'
    ### email configs,https://pythonhosted.org/Flask-Mail/
    ###
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '25'))
    MAIL_USE_SSL = False
    # enable transport layer security security ,TLS
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX_JH = '[HJiahu]'
    MAIL_SENDER_JH = os.environ.get('MAIL_SENDER_JH') # 发信者需要与所连接的smtp服务器用户名同
    # 这里是管理员所使用的邮箱，原始的 flasky 使用的变量名是 FLASKY_ADMIN
    MAIL_ADMIN_EMAIL_JH = os.environ.get('MAIL_ADMIN_EMAIL_JH','hjiahu@outlook.com')


    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    MAIL_SERVER    = 'smtp.163.com'
    MAIL_USERNAME  = 'jiahuhenan'
    MAIL_PASSWORD  = 'jiahu123'
    MAIL_SENDER_JH = 'jiahuhenan@163.com'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
