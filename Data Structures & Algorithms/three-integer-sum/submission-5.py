class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indices = []
        nums.sort()
        for i,a in enumerate(nums):
            if i == 0 or nums[i] != nums[i-1]:
                l = i + 1
                r = len(nums) - 1
                target = -a
                while r > l:
                    if nums[l] + nums[r] > target:
                        r = r - 1
                    elif nums[l] + nums[r] < target:
                        l = l + 1
                    else:
                        indices.append([a, nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                        
        return indices

            
                
        