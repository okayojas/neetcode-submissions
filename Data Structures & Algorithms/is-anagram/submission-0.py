class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sum1 = 0
        sum2 = 0

        for i in s:
            sum1 += hash(i)
        for j in t:
            sum2 += hash(j)
        
        if (sum1 == sum2):
            return True
        return False