class RecipientDB:
    def __init__(self, db):
        self.table = db.table('recipients')

    def add(self, recipient):
        self.table.insert(recipient)
        return self.table.all()

    def remove(self, recipient_id):
        sn = self.table.get(doc_id=recipient_id)
        self.table.remove(doc_ids=[recipient_id])
        return sn

    def all(self):
        return self.table.all()
