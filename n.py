# class Solution:
#     def removeDuplicateLetters(s: str) -> str:
#         seen = []
#         string = ''
#         for i in range(len(s)):
#             if s[i] not in seen:
#                 seen.append(s[i])
#                 string += s[i]
#         return string

# print(Solution.removeDuplicateLetters('affan'))

# class Solution:
    
#     def maxArea(self, height) -> int:
#         left = 0
#         right = len(height) - 1
#         maxLeft = height[left]
#         maxRight = height[right]
#         capacity = 0
#         while left <= right:
#             if maxRight > maxLeft:
#                 left += 1
#                 maxLeft = min(maxLeft, maxRight)
#                 current = height[left]
#                 current_area = maxLeft - current
#                 if current_area > 0:
#                     capacity += current_area
#                 else:
#                     capacity += 0
#             else:
#                 right -= 1
#                 maxRight = min(maxLeft, maxRight)
#                 current = height[right]
#                 current_area = maxRight - current
#                 if current_area > 0:
#                     capacity += current_area
#                 else:
#                     capacity += 0
#         return capacity
 

# # print(Solution.common(7, 7))
# height = [1,8,6,2,5,4,8,3,7]
# s = Solution()
# s.maxArea(height)

# name = 'affan'
# print(len(name))

# from collections import Counter

# nums = [-1,2,-1,4,3,2,1]
# print(nums.pop())

# print(nums.pop())
# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == 5:
#         break
s = [1]
if s:
    print('y')
else:
    print('n')
