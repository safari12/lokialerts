import smtplib
import os
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer:
    def __init__(self, user, password, recipients):
        self.server = None
        self.user = user
        self.recipients = recipients
        self.password = password

    def connect(self):
        try:
            self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.server.login(self.user, self.password)
            self.server.ehlo()
        except smtplib.SMTPException as e:
            print('Unable to connect to gmail server %s' % str(e))
            sys.exit()

    def send(self, message):
        msg = MIMEMultipart()
        msg['From'] = self.user
        msg['To'] = self.recipients
        msg['Subject'] = 'CryptoAlerts'
        msg.attach(MIMEText(message, 'plain'))
        self.server.send_message(msg)
        del msg

    def disconnect(self):
        self.server.close()