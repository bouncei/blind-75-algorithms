# Approach
# 1. Create ans array to store the output values and fill the array with 0.
# 2. Count the number of zeros in the nums array and store it in zeros variable.
# 3. Calculate the product of non-zero elements in the nums array and store it in the product variable.
#     Now focus on the count of zeros:
#     -if the count of zeros are 1, which means output of each non-zero element of the nums array in the ans array will be equal to 0 (zero). And output of the one and only zero element of the nums array in the ans array will be equal to product.
#     -if the count of zeros are 0, which means all the elements in the nums array are non-zero and output of each element of the nums array in the ans array will be equal to product / nums[i].
#     -if the count of zeros are 2 or more than 2, which means output of all the elements of the nums array in the ans array will be equal to 0.



class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        ans = [0] * n
        product = 1
        zeros = 0


        for num in nums:
            if num == 0:
                zeros += 1
                continue
            
            product *= num

        
        if zeros == 1:
            for i in range(n):
                ans[i] = product if nums[i] == 0 else 0

        elif zeros == 0:
            for i in range(n):
                ans[i] = product // nums[i]


        return ans