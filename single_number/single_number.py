'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    # find max val in arr
    max_val = arr[0]
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            max_val = arr[i+1]

    # intialize array of zeros
    initialiazed_arr = [0] * (max_val+1)

    # count how many times a number appears in arr
    for value in arr:
        for i in range(len(initialiazed_arr)):
            if value == i:
                initialiazed_arr[i] += 1

    # find the value that appears only once:
    for i in range(len(initialiazed_arr)):
        if initialiazed_arr[i] == 1:
            return i

    return arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")