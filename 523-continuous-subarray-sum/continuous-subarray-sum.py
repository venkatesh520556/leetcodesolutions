class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0: -1}   # mod → first index
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            mod = curr_sum % k

            if mod in hashmap:
                if i - hashmap[mod] > 1:
                    return True
            else:
                hashmap[mod] = i

        return False

        