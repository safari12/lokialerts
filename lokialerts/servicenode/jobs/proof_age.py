import time
import click

from lokialerts.servicenode.constants import PROOF_AGE_WARNING
from lokialerts.servicenode.jobs.base import BaseJob
from requests.exceptions import RequestException
from lokialerts.servicenode.rpc import ServiceNodeRPCError


class ServiceNodeProofAgeJob(BaseJob):
    def schedule(self, scheduler):
        scheduler.every(10).seconds.do(self.run)

    def run(self):
        click.echo("Checking last uptime proof")
        for sn in self.db.all():
            try:
                stats = self.rpc.get_service_node_stats(sn)
                last_uptime_proof = stats['last_uptime_proof']
                proof_age = int(time.time() - last_uptime_proof)
                if last_uptime_proof != 0 and proof_age >= PROOF_AGE_WARNING:
                    click.echo(
                        "Service node %s has extended proof age warning, notifying users"
                        % sn['label']
                    )
                    if self.mailer.connect():
                        self.mailer.send(
                            'Service node %s proof age is too high, please check node' % sn['label'],
                            self.recipient_db.all()
                        )
                        self.mailer.disconnect()
            except ServiceNodeRPCError:
                click.secho(
                    'Unable to get stats from %s service node rpc' % sn['label'],
                    fg='red'
                )
