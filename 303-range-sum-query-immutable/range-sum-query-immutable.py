class NumArray:

    def __init__(self, nums: List[int]):
        self.result = [0] * len(nums)
        self.result[0] = nums[0]
        for i in range(1,len(nums)):
            self.result[i] = self.result[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.result[right]
        left_sum = self.result[left-1] if left > 0 else 0
        return right_sum - left_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)