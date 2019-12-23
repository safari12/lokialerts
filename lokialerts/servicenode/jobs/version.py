import time
import click

from lokialerts.servicenode.jobs.base import BaseJob
from lokialerts.servicenode import util
from lokialerts.servicenode.rpc import ServiceNodeRPCError
from lokialerts.github import LokiGithubError


class ServiceNodeVersionJob(BaseJob):
    def __init__(self, mailer, rpc, db, github):
        super().__init__(mailer, rpc, db)
        self.github = github

    def schedule(self, scheduler):
        scheduler.every().hour.do(self.run)

    def run(self):
        try:
            latest_version = self.github.get_latest_version()
            s_nodes = self.db.all()
            for sn in s_nodes:
                stats = self.rpc.get_service_node_stats(sn)
                current_version = util.parse_version(
                    stats['service_node_version'])
                if current_version < latest_version:
                    click.echo("Service node is out to date")
                    click.echo("Notifying users")
                    self.mailer.connect()
                    self.mailer.send(
                        """Service node %s version is %s and the latest version is %s, 
                        please update node""" % (sn['label'], current_version, latest_version)
                    )
                    self.mailer.disconnect()
        except LokiGithubError:
            click.secho(
                'ServiceNodeVersionJob - Unable to get latest version from github', fg='red')
        except ServiceNodeRPCError:
            click.secho(
                'ServiceNodeVersionJob - Unable to get service node stats for %s from rpc' % sn['label'], fg='red')
