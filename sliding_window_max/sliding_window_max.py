'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    # keep track of what our window is
    window = []
    # keep track of our max_vals array
    max_vals = []

    for i in range(len(nums)-1):
        window = nums[i:i+k]
        if len(window) == k:
            max_vals.append(max(window))

    return max_vals


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
