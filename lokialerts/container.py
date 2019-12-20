import os

from tinydb import TinyDB
from pathlib import Path

from lokialerts.servicenode import ServiceNodeTable, ServiceNodeDB, inquirer
from lokialerts.mailer import Mailer

app_path = '%s/.lokialerts' % Path.home()
data_path = app_path + '/data.json'

if not os.path.exists(app_path):
    os.makedirs(app_path)
db = TinyDB(data_path)


mailer = Mailer(
    os.getenv('MAILER_USER'),
    os.getenv('MAILER_PASSWORD'),
    os.getenv('MAILER_RECIPIENTS')
)

service_node_db = ServiceNodeDB(db)
service_node_table = ServiceNodeTable()
service_node_inquirer = inquirer
