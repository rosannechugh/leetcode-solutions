class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        seen={}
        output=[]
        for i in nums:
            seen[i]=seen.get(i,0)+1
        for _ in range(k):
            max_key=max(seen,key=seen.get)
            output.append(max_key)
            seen.pop(max_key)
        return output