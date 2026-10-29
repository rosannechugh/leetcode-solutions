class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        start=0
        max_len=1
        for i in range(n):
            left,right=i,i
            while left>=0 and right<n and s[left]==s[right]:
                if right-left+1>max_len:
                    start=left
                    max_len=right-left+1
                left-=1
                right+=1
            left,right=i,i+1
            while left>=0 and right<n and s[left]==s[right]:
                if right-left+1>max_len:
                    start=left
                    max_len=right-left+1
                left-=1
                right+=1
        return s[start:start+max_len]
        
                        