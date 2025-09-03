class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        result = sum(arr)
        target = result // 3
        if result % 3 != 0:
            return False
        curr = 0
        count = 0
        for i in range(len(arr)-1):
            curr += arr[i]
            if curr == target:
                count += 1
                curr = 0
            if count == 2:
                return True
        return False
        