'''
Input: an integer
Returns: an integer
'''

    # combine all recursion calls
    # remember about - cases
def eating_cookies(n):
    # Your code here
    # keep track of number of iterations
    counter = 0

    counter += 1
    # Base case:
    # if there is no cookies or we hit negative numbers, return counter
    if n <= 0 :
        return counter

    # when there is at least 3, we can use 1s 2s and 3s
    if n>=3:
        return(eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))
    # when there at least 2, we can use 1s 2s 
    if n>=2:
        return(eating_cookies(n-1) + eating_cookies(n-2))
    # when there is at least 1 cookie, we can only play with 1s
    if n>=1:
        return(eating_cookies(n-1))

    return counter


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

''' eating cookies DAY 2'''
def eating_cookies(n, cache={}):
    counter = 0
    counter += 1

    if n <= 0:
        return counter
    # if we checked for that n before and saved in our cache
    elif n in cache:
        # return the value at key/index? n
        return cache[n]
    
    # when there is at least 1 cookie, we can only play with 1s
    elif n==1:
        case1=(eating_cookies(n-1))
        cache[n] = case1 # were adding the outcome of case 1 as the value of key n
        return case1
    # when there at least 2, we can use 1s 2s 
    elif n==2:
        case2=(eating_cookies(n-1) + eating_cookies(n-2))
        cache[n] = case2
        return case2
    else:
        case3 = (eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))
        # save our recursion in cache for future use
        cache[n] = case3
        # return current case
        return case3

# my_dict = {}
# print(my_dict)
# my_dict[50] = {'aaa'}
# print(my_dict)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 50

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")