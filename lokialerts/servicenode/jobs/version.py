import time
import click

from lokialerts.servicenode.jobs.base import BaseJob
from lokialerts.servicenode import util
from lokialerts.servicenode.rpc import ServiceNodeRPCError
from lokialerts.github import LokiGithubError


class ServiceNodeVersionJob(BaseJob):
    def __init__(self, mailer, rpc, db, recipient_db, github):
        super().__init__(mailer, rpc, db, recipient_db)
        self.github = github

    def schedule(self, scheduler):
        scheduler.every(15).seconds.do(self.run)

    def run(self):
        s_nodes = self.db.all()

        if len(s_nodes) == 0:
            click.echo("No service nodes to check version")
            return

        try:
            latest_version_tag = self.github.get_latest_version()
            latest_version = util.parse_version_tag(latest_version_tag)
            for sn in s_nodes:
                click.echo("Checking version for %s" % sn['label'])
                stats = self.rpc.get_service_node_stats(sn)
                current_version_tag = stats['service_node_version']
                current_version = util.parse_version(current_version_tag)
                if current_version != 0 and current_version < latest_version:
                    click.echo("Service node %s is out to date" % sn['label'])
                    click.echo("Notifying users")
                    self.mailer.connect()
                    self.mailer.send(
                        """Service node %s version is %s and the latest version is %s, 
                        please update node""" % (sn['label'], util.parse_version_arr(current_version_tag), latest_version_tag),
                        self.recipient_db.all()
                    )
                    self.mailer.disconnect()
                else:
                    click.echo(
                        "Version is up to date for service node %s" % sn['label']
                    )
        except LokiGithubError:
            click.secho(
                'ServiceNodeVersionJob - Unable to get latest version from github', fg='red')
        except ServiceNodeRPCError:
            click.secho(
                'ServiceNodeVersionJob - Unable to get service node stats for %s from rpc' % sn['label'], fg='red')
