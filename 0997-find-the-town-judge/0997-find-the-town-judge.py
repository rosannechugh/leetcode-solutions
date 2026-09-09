class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        for i in range(1,n+1):
            trusted_by=0
            trusts_someone=False
            for a,b in trust:
                if a==i:
                    trusts_someone=True
                elif b==i:
                    trusted_by+=1
            if trusted_by==n-1 and not trusts_someone:
                return i
        return -1