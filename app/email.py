from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
import time
from . import mail


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
            # 有些网站把连接很短的请求当作恶意访问
        except Exception as e:
            app.logger.debug('********* error in send_async_email:mail.send(msg) *********\n'+str(e))



def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_SUBJECT_PREFIX_JH'] + ' ' + subject,
                  sender=app.config['MAIL_SENDER_JH'], recipients=[to])

    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
