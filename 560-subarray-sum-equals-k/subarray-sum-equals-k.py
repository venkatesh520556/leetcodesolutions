class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        result = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum == k:
                result += 1
            if curr_sum - k in hashmap:
                result += hashmap[curr_sum - k]
            hashmap[curr_sum] = hashmap.get(curr_sum,0) + 1
        return result