import os

from tinydb import TinyDB
from pathlib import Path

from lokialerts.servicenode import ServiceNodeTable, ServiceNodeDB, ServiceNodeStatusJob, ServiceNodeRPC, inquirer
from lokialerts.mailer import Mailer
from lokialerts.scheduler import Scheduler

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

sn_db = ServiceNodeDB(db)
sn_table = ServiceNodeTable()
sn_inquirer = inquirer
sn_rpc = ServiceNodeRPC()

scheduler = Scheduler([
    ServiceNodeStatusJob(mailer, sn_rpc, sn_db)
])
