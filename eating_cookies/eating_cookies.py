'''
Input: an integer
Returns: an integer
'''

def eating_cookies(n):
    # Your code here
    # keep track of number of iterations
    counter = 0

    counter += 1
    # Base case:
    # if there is no cookies, return 1
    if n <= 0 :
        return counter
    # if we hit a negative case, just return

    # eat 3 cookie at a time
    if n>=3:
        return(eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))
    if n>=2:
        return(eating_cookies(n-1) + eating_cookies(n-2))
    if n>=1:
        return(eating_cookies(n-1))

    return counter

    # combine all recursion calls
    # remember about - cases

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
