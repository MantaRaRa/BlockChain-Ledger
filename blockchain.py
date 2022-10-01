from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = {}
        previous_hash = '0'
        self.chain.append(Block(transactions, previous_hash))

    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_block()

    def add_block(self, transactions):
        previous_hash = self.chain[-1].hash
        new_block = Block(transactions, previous_hash)
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print("The current hash of the block doesn't equal the hash of the block")
            if current.previous_hash != previous.hash:
                print("The previous hash of the current block isn't equal to the previous block's hash")
                return False
            return True

    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:difficulty] != '0' * difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        print("Successfully mined block. Hash: {}".format(proof))
        return proof


