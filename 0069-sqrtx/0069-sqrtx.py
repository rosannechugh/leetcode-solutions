class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low=0
        high=x
        ans=0
        while low<=high:
            middle=(low+high)//2
            if middle*middle==x:
                return middle
            elif x>middle*middle:
                ans=middle
                low=middle+1
                middle=(low+high)//2
                if middle*middle==x:
                    return middle
            elif x<middle*middle:
                high=middle-1
                middle=(low+high)//2
                if middle*middle==x:
                    return middle
        return ans