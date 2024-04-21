class InMemoryDB:
    def __init__(self):
        self.main_state = {}
        self.transaction_state = None
        self.in_transaction = False

    def begin_transaction(self):
        if self.in_transaction:
            raise Exception("Transaction already in progress")
        self.in_transaction = True
        self.transaction_state = self.main_state.copy()

    def put(self, key, value):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        self.transaction_state[key] = value

    def get(self, key):
        if self.in_transaction:
            return self.transaction_state.get(key, None)
        return self.main_state.get(key, None)

    def commit(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        self.main_state = self.transaction_state.copy()
        self.in_transaction = False
        self.transaction_state = None

    def rollback(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        self.in_transaction = False
        self.transaction_state = None

if __name__ == "__main__":
    db = InMemoryDB()
    print(db.get("A"))
    try:
        db.put("A", 5)
    except Exception as e:
        print(e)

    db.begin_transaction()
    db.put("A", 5)
    print(db.get("A"))
    db.put("A", 6)
    print(db.get("A"))
    db.commit()
    print(db.get("A"))

    try:
        db.commit()
    except Exception as e:
        print(e)

    try:
        db.rollback()
    except Exception as e:
        print(e)

    print(db.get("B"))
    db.begin_transaction()
    db.put("B", 10)
    db.rollback()
    print(db.get("B"))
