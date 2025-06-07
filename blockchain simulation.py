import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + self.timestamp + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()


blockchain = [Block(0, time.ctime(), "Genesis Block")]

for i in range(1, 3):
    prev_block = blockchain[i-1]
    new_block = Block(i, time.ctime(), f"Block {i} Data", prev_block.hash)
    blockchain.append(new_block)


for block in blockchain:
    print(f"Block {block.index}:")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print()


print("Tampering with Block 1...\n")
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].calculate_hash()


for block in blockchain:
    print(f"Block {block.index} recalculated:")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print()
