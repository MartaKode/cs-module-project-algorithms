'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here

    zeros = []
    nonzeros = []

    for i in arr:
        if i == 0:
            zeros.append(i)
        else: 
            nonzeros.append(i)

    return nonzeros + zeros


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
