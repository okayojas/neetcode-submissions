class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = defaultdict(int)
        answers = []
        for i in nums:
            numbers[i] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in numbers.items():
            buckets[freq].append(num)
        
        for f in range(len(nums), 0, -1):
            for num in buckets[f]:
                answers.append(num)
                k-= 1
                if k == 0:
                    return answers
        
            

        return answers

        