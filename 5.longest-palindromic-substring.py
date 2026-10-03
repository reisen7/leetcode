#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30204
#
# [5] 最长回文子串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1

                else:
                    break
            # print("结果为：" + s[left + 1 : right])
            return s[left + 1 : right]

        ans = ""
        for i in range(len(s)):
            tmp = expand(i, i)
            if len(tmp) >= len(ans):
                ans = tmp
            tmp = expand(i, i + 1)
            if len(tmp) >= len(ans):
                ans = tmp

        return ans


# @lc code=end


#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#
