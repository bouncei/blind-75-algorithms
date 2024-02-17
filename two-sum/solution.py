class Solution(object):
    def twoSum_1(self, nums, target): #TIME COMPLEXITY O(n) ([BEST CASE])
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numToIndex = {} #using a hash map to reduce the time complexity
        for index in range(len(nums)):
            if target - nums[index] in numToIndex:
                return [numToIndex[target - nums[index]], index]
            numToIndex[nums[index]] = index
        return []
    


    def twoSum_2(self, nums, target): #TIME COMPLEXITY: O(n^2)
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        reference_index = 0
        a = nums[reference_index]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i, j]

        return []

