import time
import click

from lokialerts.servicenode.constants import PROOF_AGE_WARNING
from requests.exceptions import RequestException


class ServiceNodeStatusJob:
    def __init__(self, mailer, rpc, db):
        self.mailer = mailer
        self.rpc = rpc
        self.db = db

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
