'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    # factorial function!
    no_index_arr = []
    factorial_arr = []
    factorial = 1
    for i in range(len(arr)-1): # maybe dont need double for loop?
        no_index_arr = arr[:i] + arr[i+1:]
        for value in no_index_arr:
            factorial *= value
        factorial_arr.append(factorial)
        factorial = 1

    # to include last value:
    arr.pop()
    for value in arr:
        factorial *= value
    factorial_arr.append(factorial)

    return factorial_arr

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

'''DAY 2'''
# fixed space complexity 
def product_of_all_other_numbers(arr):
    # factorial function!
    factorial_arr=[]
    factorial = 1
    for i in range(len(arr)-1): # maybe dont need double for loop?
        # pop out index 
        popped_index = arr.pop(i)
        for value in arr:
            # perform factorial
            factorial *= value
        # add index back
        arr.insert(i, popped_index)
        
        factorial_arr.append(factorial)
        factorial = 1

    # to include last value:
    arr.pop()
    for value in arr:
        factorial *= value
    factorial_arr.append(factorial)
    return factorial_arr

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
