class ServiceNodeDB:
    def __init__(self, db):
        self.table = db.table('servicenodes')

    def add(self, sn):
        self.table.insert(sn)
        return self.table.all()

    def remove(self, sn_id):
        self.table.remove(doc_ids=[sn_id])
        return self.table.all()

    def all(self):
        return self.table.all()
