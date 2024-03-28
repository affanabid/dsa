# https://leetcode.com/problems/3sum/

# class Solution:
    
def threeSum(nums):
    nums.sort()
    n = len(nums)
    result = []
    i = 0

    while i < n:
        value = nums[i]
        target = -(value)
        j = i+1
        k = len(nums) - 1

        while j < k:
            sum_ = nums[j] + nums[k]
            if sum_ < target:
                j += 1
            elif sum_ > target:
                k -= 1
            else:
                result.append([nums[i], nums[j], nums[k]])
        i += 1

    return result

def main():
    nums = [-1,0,1,2,-1,-4]

    print(threeSum(nums))
main()