class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n=len(matrix)
        ans=[0]*n
        for i in range(n):
            for j in range(n):
                ans[i]+=matrix[i][j]
        return ans