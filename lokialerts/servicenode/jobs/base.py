class BaseJob:
    def __init__(self, mailer, rpc, db, recipient_db):
        self.mailer = mailer
        self.rpc = rpc
        self.db = db
        self.recipient_db = recipient_db
