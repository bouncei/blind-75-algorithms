
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_str = bin(n)[2:] #convert str to binary format
        count = Counter(binary_str)

        print(count)


        return count["1"]
        