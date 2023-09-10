class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        dict1 = {}
        for i in nums:
            if k-i in dict1 and dict1[k-i] != 0:
                res += 1
                dict1[k-i] -= 1
            else:
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1

        return res
