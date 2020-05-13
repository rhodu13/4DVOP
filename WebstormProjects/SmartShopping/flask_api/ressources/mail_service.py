from asyncio import sleep
from threading import Thread
from flask_mail import Message

sleep(10)

from flask import current_app as app
from flask import current_app as mail


def send_async_email(flask_app, msg):
    with flask_app.app_context():
        try:
            mail.send(msg)
        except ConnectionRefusedError:
            raise InternalServerError("[MAIL SERVER] not working")


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()
