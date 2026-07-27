class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = []
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum > target:
                j-= 1
            elif sum < target:
                i+= 1
            else:
                nums.append(i+1)
                nums.append(j+1)
                return nums
