import time
import click

from lokialerts.servicenode.jobs.base import BaseJob
from lokialerts.servicenode import util
from requests.exceptions import RequestException


class ServiceNodeVersionJob(BaseJob):
    def __init__(self, mailer, rpc, db, github):
        super(mailer, rpc, db)
        self.github = github

    def set_schedule(self, schedule):
        schedule.every().day.at('8:00').do(self.run)
        schedule.every().day.at('12:00').do(self.run)
        schedule.every().day.at('18:00').do(self.run)

    def run(self):
        latest_version = self.github.get_latest_version()
        s_nodes = self.db.all()
        for sn in s_nodes:
            stats = self.rpc.get_service_node_stats(sn)
            current_version = util.parse_version(stats['service_node_version'])
            if current_version < latest_version:
                click.echo("Service node is out to date")
                click.echo("Notifying users")
                self.mailer.connect()
                self.mailer.send(
                    """Service node %s version is %s and the latest version is %s, 
                    please update node""" % (sn['label'], current_version, latest_version)
                )
                self.mailer.disconnect()
