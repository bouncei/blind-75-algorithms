from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
       
        left, right = 0, len(height) - 1 # Using two pointer approach

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right])) 

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
           

            
        return max_area
        
