class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        currentstreak=1
        longeststreak=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                currentstreak+=1
            if nums[i]!=nums[i-1]+1:
                currentstreak=1
            
            if currentstreak>longeststreak:
                longeststreak=currentstreak
        return longeststreak


        