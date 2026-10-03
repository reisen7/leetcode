#
# @lc app=leetcode.cn id=4 lang=python
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        n = len(merged)
        if n % 2 == 1:
            return merged[n // 2]
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0


# @lc code=end


#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,4,4]\n[2,2,2,4,4]\n
# @lcpr case=end
