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
        sn_nodes = self.db.all()

        if len(sn_nodes) == 0:
            click.echo("No service nodes to check uptime proof")

        for sn in sn_nodes:
            try:
                click.echo("Checking last uptime proof for %s" % sn['label'])
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
                else:
                    click.echo(
                        "Last Uptime Proof is correct for service node %s" % sn['label']
                    )
            except ServiceNodeRPCError:
                click.secho(
                    'Unable to get stats from %s service node rpc' % sn['label'],
                    fg='red'
                )
