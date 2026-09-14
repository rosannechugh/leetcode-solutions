class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen={0:1}
        current_sum=0
        count=0
        for num in nums:
            current_sum+=num
            if current_sum - k in seen:
                count+=seen[current_sum-k]
            seen[current_sum]=seen.get(current_sum,0)+1
        return count
    
            
