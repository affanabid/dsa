# https://leetcode.com/problems/3sum/

class Solution:
    
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        i = 0
        while i < n:
            value = nums[i]
            target = -(value)
            j = i+1
            k = len(nums) - 1
            while j != k:
                sum = nums[j] + nums[k]
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
            i += 1
        return result

