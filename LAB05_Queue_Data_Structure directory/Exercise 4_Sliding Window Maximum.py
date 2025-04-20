from collections import deque

def sliding_window_max(nums, k):
    if not nums or k == 0:
        return []

    max_values = []
    dq = deque()

    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            max_values.append(nums[dq[0]])

    return max_values

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = sliding_window_max(nums, k)
print("Input:", nums)
print("Window size:", k)
print("Sliding window maximums:", result)
