from blockchain import Blockchain

block_one_transactions = {"Sender": "WrightPatt Credit Union", "Receiver": "Von", "Amount": "100,000"}
block_two_transactions = {"Sender": "Von", "Receiver": "Sarah", "Amount": "50,000"}
block_three_transactions = {"Sender": "Sarah", "Receiver": "Everleigh", "Amount": "25,000"}
fake_transactions = {"Sender": "Von", "receiver": "Sarah, Everleigh", "Amount": "125,000"}

blockchain = Blockchain()
blockchain.print_blocks()

blockchain.add_block(block_one_transactions)
blockchain.add_block(block_two_transactions)
blockchain.add_block(block_three_transactions)
blockchain.print_blocks()
blockchain.chain[2].transactions = fake_transactions
blockchain.validate_chain()
