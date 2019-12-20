import os

from tinydb import TinyDB
from pathlib import Path

from lokialerts.servicenode import ServiceNodeTable, ServiceNodeDB, inquirer

app_path = '%s/.lokialerts' % Path.home()
data_path = app_path + '/data.json'

if not os.path.exists(app_path):
    os.makedirs(app_path)
db = TinyDB(data_path)

service_node_db = ServiceNodeDB(db)
service_node_table = ServiceNodeTable()
service_node_inquirer = inquirer
