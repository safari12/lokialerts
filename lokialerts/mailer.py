import smtplib
import os
import sys
import click

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer:
    def __init__(self, user, password):
        self.server = None
        self.user = user
        self.password = password

    def connect(self):
        try:
            self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.server.login(self.user, self.password)
            self.server.ehlo()
            return True
        except smtplib.SMTPException as e:
            click.echo('Unable to connect to gmail server %s' % str(e))
            return False

    def send(self, message, recipients):
        msg = MIMEMultipart()
        msg['From'] = self.user
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = 'CryptoAlerts'
        msg.attach(MIMEText(message, 'plain'))
        self.server.send_message(msg)
        del msg

    def disconnect(self):
        self.server.close()
