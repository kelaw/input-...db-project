import hashlib as hasher


class Block:
    no_of_instances = 0

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

        Block.no_of_instances += 1

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) +
                    str(self.data) + str(self.previous_hash)).encode("utf-8"))
        return sha.hexdigest()





