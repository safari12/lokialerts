class BaseJob:
    def __init__(self, mailer, rpc, db):
        self.mailer = mailer
        self.rpc = rpc
        self.db = db
