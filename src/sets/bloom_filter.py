import hashlib
import math
from bitarray import bitarray


class BloomFilter:
    def __init__(self, expected_items, false_positive_rate):
        self.n = expected_items
        self.p = false_positive_rate

        # Calculate optimal size of bit array (m) and number of hash functions (k)
        self.m = self._optimal_bit_array_size(self.n, self.p)
        self.k = self._optimal_hash_count(self.m, self.n)

        self.bit_array = bitarray(self.m)
        self.bit_array.setall(0)

    def _hashes(self, item):
        # Create k hash values using double hashing technique
        item = item.encode("utf-8")
        hash1 = int(hashlib.md5(item).hexdigest(), 16)
        hash2 = int(hashlib.sha1(item).hexdigest(), 16)

        for i in range(self.k):
            yield (hash1 + i * hash2) % self.m

    def add(self, item):
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def __contains__(self, item):
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))

    @staticmethod
    def _optimal_bit_array_size(n, p):
        """m = -(n * ln(p)) / (ln(2)^2)"""
        return int(-(n * math.log(p)) / (math.log(2) ** 2))

    @staticmethod
    def _optimal_hash_count(m, n):
        """k = (m/n) * ln(2)"""
        return int((m / n) * math.log(2))


# ---------------------------
# 🔬 Example usage:
# ---------------------------
def main():
    bf = BloomFilter(expected_items=1000, false_positive_rate=0.01)

    # Add elements
    bf.add("apple")
    bf.add("banana")
    bf.add("orange")

    # Query
    print("apple" in bf)  # True
    print("banana" in bf)  # True
    print("cherry" in bf)  # False (probably)

    # A word not added might still return True due to false positives
    print("pineapple" in bf)  # Might be True (false positive)


if __name__ == "__main__":
    main()
