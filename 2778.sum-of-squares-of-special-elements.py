#
# @lc app=leetcode.cn id=2778 lang=python3
# @lcpr version=30204
#
# [2778] 特殊元素平方和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        ans = []
        length = len(nums)
        for i,x in enumerate(nums):
            j = i + 1
            if j  and length % j == 0:
                ans.append(x*x)
        return sum(ans) 
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,1,19,18,3]\n
# @lcpr case=end

#

