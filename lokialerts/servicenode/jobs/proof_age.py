import time
import click

from lokialerts.servicenode.constants import PROOF_AGE_WARNING
from lokialerts.servicenode.jobs.base import BaseJob
from requests.exceptions import RequestException


class ServiceNodeProofAgeJob(BaseJob):
    def set_schedule(self, schedule):
        schedule.every(10).minutes.do(self.run)

    def run(self):
        for sn in self.db.all():
            try:
                last_uptime_proof = self.rpc.get_service_nodes(
                    ip=sn['ip'],
                    port=sn['port'],
                    pubkeys=[sn['pubkey']]
                )
                proof_age = int(time.time() - last_uptime_proof)
                if proof_age >= PROOF_AGE_WARNING:
                    click.echo(
                        "Service node %s has extended proof age warning, notifying users"
                        % sn['label']
                    )
                    self.mailer.connect()
                    self.mailer.send(
                        'Service node %s proof age is too high, please check node' % sn['label']
                    )
                    self.mailer.disconnect()
            except RequestException:
                click.echo(
                    'Unable to connect to %s service node' % sn['label']
                )
