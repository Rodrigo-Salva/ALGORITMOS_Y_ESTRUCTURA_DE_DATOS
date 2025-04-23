from collections import deque

def sliding_window_max(nums, k):
    if not nums or k == 0:
        return []

    max_values = []
    q = deque()

    for i in range(len(nums)):
        if q and q[0] < i - k + 1:
            q.popleft()
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        q.append(i)
        if i >= k - 1:
            max_values.append(nums[q[0]])
    return max_values

# Test
def run_tests():
    return (
        sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7] and
        sliding_window_max([9, 9, 9, 9], 2) == [9, 9, 9] and
        sliding_window_max([4, 2, 12, 11, -5], 1) == [4, 2, 12, 11, -5] and
        sliding_window_max([1, 2, 3, 4, 5], 5) == [5] and
        sliding_window_max([], 3) == [] and
        sliding_window_max([1, 2, 3], 0) == []
    )
    
print(run_tests())



