class Solution:
    def groupAnagrams(self, strs):
        groups = []
        for i in range(len(strs)):
            if strs[i] != -1:
                group = []
                group.append(strs[i])
                current = sorted(strs[i])
                for j in range(i+1, len(strs)):
                    temp = sorted(strs[j])
                    if len(current) == len(temp) and current == temp:
                        group.append(strs[j])
                        strs[j] = -1
            groups.append(group)
        return groups

strs = ["eat","tea","tan","ate","nat","bat"]

s = Solution()
s.groupAnagrams(strs)