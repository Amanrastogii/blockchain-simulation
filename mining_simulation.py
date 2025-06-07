import hashlib
import time

class Block:
    def __init__(self, index, data):
        self.index = index
        self.timestamp = time.ctime()
        self.data = data
        self.previous_hash = ""
        self.nonce = 0
        self.hash = ""

    def calculate_hash(self):
        value = str(self.index) + self.timestamp + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        start_time = time.time()
        print(f"Mining block {self.index}...")
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith('0' * difficulty):
                break
            self.nonce += 1
        end_time = time.time()
        print(f"Block mined: {self.hash}")
        print(f"Nonce: {self.nonce}")
        print(f"Time taken: {end_time - start_time:.2f} seconds\n")

difficulty = 4
block = Block(1, "Mining Demo")
block.mine_block(difficulty)
