class Solution(object):
    def minCost(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)

        right = []
        left = []

        for i in range(n - 1):
            gap = nums[i + 1] - nums[i]

            # Cost to move from i to i + 1
            if i == 0 or gap < nums[i] - nums[i - 1]:
                right.append(1)
            else:
                right.append(gap)

            # Cost to move from i + 1 to i
            if i == n - 2 or gap <= nums[i + 2] - nums[i + 1]:
                left.append(1)
            else:
                left.append(gap)
        prefixRight = [0] * n
        prefixLeft = [0] * n

        for i in range(1, n):
            prefixRight[i] = prefixRight[i - 1] + right[i - 1]

        for i in range(1, n):
            prefixLeft[i] = prefixLeft[i - 1] + left[i - 1]
        ans = []

        for l, r in queries:
            if l < r:
                ans.append(prefixRight[r] - prefixRight[l])
            elif l > r:
                ans.append(prefixLeft[l] - prefixLeft[r])
            else:
                ans.append(0)

        return ans