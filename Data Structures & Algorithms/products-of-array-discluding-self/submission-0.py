class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix=1
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i]=prefix
            prefix=prefix*nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
             ans[i]=ans[i]*suffix
             suffix=suffix*nums[i]
        return ans