class Solution(object):
    def removeElement(self, nums, val):
        nums.sort()
        j=0
        while j<len(nums):
            if nums[j]==val:
                nums.pop(j)
            else:
                j+=1
                
        return len(nums)
        