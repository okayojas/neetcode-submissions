class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = []
        for i,n in enumerate(numbers):
            nums.append(i+1)
            for j in range(i+1, len(numbers)):
                if n + numbers[j] == target:
                    nums.append(j+1)
                    return nums
            nums = []
