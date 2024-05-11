class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = nums[0]
        curr = nums[0]

   
        for num in nums[1:]:
            curr = max(num, curr + num)
            ans = max(ans,curr)
        return ans

        