class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_arr = [0] * len(nums)
        prefix_arr[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_arr[i] = prefix_arr[i-1] + nums[i]
        return prefix_arr
        