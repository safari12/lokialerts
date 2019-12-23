import os

from tinydb import TinyDB
from pathlib import Path

from lokialerts.servicenode import ServiceNodeTable, ServiceNodeDB, ServiceNodeProofAgeJob, ServiceNodeVersionJob, ServiceNodeRPC, inquirer
from lokialerts.mailer import Mailer
from lokialerts.scheduler import Scheduler
from lokialerts.github import LokiGithub
from lokialerts import recipient
from lokialerts.recipient import RecipientTable, RecipientDB

app_path = '%s/.lokialerts' % Path.home()
data_path = app_path + '/data.json'

if not os.path.exists(app_path):
    os.makedirs(app_path)
db = TinyDB(data_path)

loki_github = LokiGithub()

mailer = Mailer(
    os.getenv('MAILER_USER'),
    os.getenv('MAILER_PASSWORD'),
)

sn_db = ServiceNodeDB(db)
sn_table = ServiceNodeTable()
sn_inquirer = inquirer
sn_rpc = ServiceNodeRPC()

recipient_inquirer = recipient.inquirer
recipient_table = RecipientTable()
recipient_db = RecipientDB(db)

scheduler = Scheduler([
    ServiceNodeProofAgeJob(mailer, sn_rpc, sn_db, recipient_db),
    ServiceNodeVersionJob(mailer, sn_rpc, sn_db, recipient_db, loki_github)
])
