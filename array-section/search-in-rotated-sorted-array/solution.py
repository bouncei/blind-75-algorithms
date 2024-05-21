from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1


        numToIndex = {}

        for index in range(len(nums)):

            numToIndex[nums[index]] = index

            if target in numToIndex:
                return numToIndex[target]

        
        print(numToIndex)
        return -1

        