#
# @lc app=leetcode.cn id=3 lang=python
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        last = {}  # 字符 -> 最后一次出现的索引
        left = 0  # 窗口左边界
        ans = 0

        for right, ch in enumerate(s):
            # 如果 ch 在窗口内出现过，把左边界跳到它后面
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            ans = max(ans, right - left + 1)

        return ans


# @lc code=end


#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#
