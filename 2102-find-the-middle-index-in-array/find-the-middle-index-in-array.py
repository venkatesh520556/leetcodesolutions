class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = [None] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        for i in range(len(nums)):
            if i == 0:
                left_sum = 0
            else:
                left_sum = prefix_sum[i-1]
            right_sum = prefix_sum[len(nums)-1] - prefix_sum[i]
            if left_sum == right_sum:
                return i
        return -1