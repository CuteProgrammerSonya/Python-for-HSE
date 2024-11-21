# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/description/?envType=problem-list-v2&envId=sliding-window


def maxSlidingWindow(nums, k):
    max_window = 0
    summa = 0
    for i in range(0, k):
        summa += nums[i]
    max_window = summa
    print(summa)
    for i in range(1, len(nums) - k + 1):
        summa -= nums[i - 1]
        summa += nums[i + k - 1]
        print(summa)
        if summa >= max_window:
            max_window = summa
    return max_window


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))
