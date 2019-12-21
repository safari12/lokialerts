import time

from lokialerts.servicenode.constants import PROOF_AGE_WARNING


class ServiceNodeStatusJob:
    def __init__(self, mailer, rpc, db):
        self.mailer = mailer
        self.rpc = rpc
        self.db = db

    def run(self):
        for sn in self.db.all():
            last_uptime_proof = self.rpc.get_service_nodes(
                ip=sn['ip'],
                port=sn['port'],
                pubkeys=[sn['pubkey']]
            )
            proof_age = int(time.time() - last_uptime_proof)
            if proof_age >= PROOF_AGE_WARNING:
                self.mailer.connect()
                self.mailer.send(
                    'Service node %s proof age is too high, please check node' % sn['label']
                )
                self.mailer.disconnect()
