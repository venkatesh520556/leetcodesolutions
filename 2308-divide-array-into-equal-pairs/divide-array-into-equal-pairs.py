class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0) + 1
        for key,val in hashmap.items():
            if val % 2 != 0:
                return False
        return True
        