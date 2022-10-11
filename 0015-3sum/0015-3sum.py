class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            
            l, r = i+1, len(nums)-1
            
            while l < r:
                first = nums[i]
                threeSum = first + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                elif threeSum == 0:
                    res.append([first, nums[l], nums[r]])
                    l+=1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
            
        return res
        