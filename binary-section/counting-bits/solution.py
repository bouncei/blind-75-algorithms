class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            binary_str = bin(i)[2:]
            count = Counter(binary_str)

            ans.append(int(count["1"]))

        return ans
        