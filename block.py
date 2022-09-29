import datetime
import hashlib


class Block:
    def __init__(self, transactions, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # Number only used once
        self.hash = self.generate_hash()

    def print_block(self):
        print("Timestamp: {}".format(self.timestamp))
        print("Transactions: {}".format(self.transactions))
        print("Current Hash: {}".format(self.hash))

    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = hashlib.sha256(block_contents.encode())
        return block_hash.hexdigest()
