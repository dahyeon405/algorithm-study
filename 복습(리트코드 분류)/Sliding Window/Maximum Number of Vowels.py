class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = ['a', 'e', 'i', 'o', 'u']

        startIdx = 0
        endIdx = k-1

        vowelsCnt = 0
        for i in range(startIdx, endIdx + 1):
            if s[i] in vowels:
                vowelsCnt += 1

        max_cnt = vowelsCnt
        while endIdx < len(s) - 1:
            if (s[startIdx] in vowels): vowelsCnt -= 1
            
            startIdx += 1
            endIdx += 1
            if s[endIdx] in vowels: vowelsCnt += 1
        
            max_cnt = max(vowelsCnt, max_cnt)

        return max_cnt