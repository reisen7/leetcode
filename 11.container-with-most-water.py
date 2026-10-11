#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30204
#
# [11] 盛最多水的容器
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:

        left = 0
        right = len(height) - 1

        max_value = 0
        while left < right:

            value = min(height[left] , height[right]) * (right - left)
            max_value = max(value,max_value)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_value
            


# @lc code=end



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

