# 713. Subarray Product Less Than K
# https://leetcode.com/problems/subarray-product-less-than-k/description/


def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    res = 0
    start = 0
    end = 0
    mult = 1
    while end <= len(nums) - 1:
        mult *= nums[end]
        while mult >= k:
            mult /= nums[start]
            start += 1
        res += end - start + 1
        end += 1
    return res


nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProductLessThanK(nums, k))
