from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[0,0,0]]

        ans = []
        nums.sort() # Sort the input array
        
        for index, element in enumerate(nums):
            if index > 0 and element == nums[index - 1]: # If the previous element is the same with the current element
                continue
            
            left, right = index + 1 , len(nums) - 1 # Using two pointer approach

            while left < right:
                three_sum = element + nums[left] + nums[right] # Calculate the 3 sum

                if three_sum > 0:
                    right -= 1 # Decrease the right pointer
                elif three_sum < 0:
                    left += 1 # Increase the left pointer
                else:
                    ans.append([element, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1

        return ans

        
  