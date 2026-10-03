#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30204
#
# [22] 括号生成
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        ans = []
        path = []

        def dfs(left: int, right: int):

            if len(path) == 2 * n:
                ans.append("".join(path))
                return

            if left < n:
                path.append("(")
                dfs(left + 1, right)
                path.pop()

            if right < left:
                path.append(")")
                dfs(left, right + 1)
                path.pop()

        dfs(0, 0)
        return ans


# @lc code=end


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
