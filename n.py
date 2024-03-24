class Solution:
    def removeDuplicateLetters(s: str) -> str:
        seen = []
        string = ''
        for i in range(len(s)):
            if s[i] not in seen:
                seen.append(s[i])
                string += s[i]
        return string

print(Solution.removeDuplicateLetters('affan'))