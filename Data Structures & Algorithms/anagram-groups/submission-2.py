class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        anagrams = defaultdict(list)
        for word in strs:
            sum = "".join(sorted(word))
            anagrams[sum].append(word)
        return list(anagrams.values())



        