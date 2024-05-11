class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numToIndex = {} # Hash map

        for index in range(len(nums)):
            if nums[index] in numToIndex :
                return True
                
            numToIndex[nums[index]] = index

        return False




        