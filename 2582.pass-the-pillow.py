#
# @lc app=leetcode.cn id=2582 lang=python3
# @lcpr version=30204
#
# [2582] 递枕头
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        if time < n:
            return time + 1
        else:
            # 假设n = 4 time = 9
            # 递枕头的示意图如下所示
            #      1    2    3    4    5    6    7    8    9    10   11  12
            # 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1
            # 这里能看到如果是开头或结尾的数字是重复的，因此就要去除
            # 1 -> 2 -> 3 -> 4 -> 4 -> 3 -> 2 -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 3 -> 2 -> 1
            # 用式子判断一下，必须满足每次循环的要大于time，设置 x 为所需循环的次数
            # x * 4 - (x - 1) > 9 + 1
            # 我们这里能看出，整体的意思就是，要满足time的最小循环次数，也就是x
            # 写出来判断就是 x * n - x > time
            # 化简出来就是 x > time / (n - 1)

            ch = time / (n - 1)

            # 这里需要判断一下，如果能整除整个式子的话，就代表当前的循环次数刚刚好传递到
            # 如果不是整数的话，就代表还不够，再加一次循环就ok

            if not ch.is_integer():
                ch = int(ch) + 1
            else:
                ch = int(ch)

            # 这里和最初的公式一样，是算去掉重复的，最终的序列有多少个
            arry = ch * n - (ch - 1)

            # 这里算的是，如果是偶数，那最终的多少个time 就是第几个
            if ch % 2 == 0:

                return arry - time

            # 如果是奇数的话，这里就反转一下
            else:
                return n - (arry - time) + 1


# @lc code=end


#
# @lcpr case=start
# 4\n9\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

#
