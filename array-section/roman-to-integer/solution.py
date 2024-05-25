class Solution:
    def romanToInt(self, s: str) -> int:
        # Creating Dictionary for Lookup
        num_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }


        result = 0

        for i in range(len(s)):
            if i < len(s) - 1 and num_map[s[i]] < num_map[s[i+1]]:
                result -= num_map[s[i]]
            else:
                result += num_map[s[i]]

        return result
        