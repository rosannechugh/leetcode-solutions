import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        condition=math.floor(n/2)
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
            if freq[num]>condition:
                return num
        