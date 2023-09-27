class Solution:
    def increasingTriplet(self, nums):
        smallest = next_smallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= next_smallest:
                next_smallest = num
            else:
                return True
        return False
