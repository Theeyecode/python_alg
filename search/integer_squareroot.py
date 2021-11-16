"""
Write a function that takes a non-negative integer and returns
the largest integer whose square is less than or equal to
the integer given.
Example:
    Assume input is integer 300.
    Then the expected output of the function should be
    17, since 17^2 = 289 < 300. Note that 18^2 = 324 > 300,
    so the number 17 is the correct response.
"""
k = 300


def find_integer_sqaure(k):
    low = 0
    high = k

    while low <= high:
        mid = (low+high) // 2
        print('mid is:', mid)
        midsq = mid*mid
        if (midsq) <= k:
            low = mid + 1
            print('low is:', low)
        else:
            high = mid - 1
            print('high is:', high)

    return low - 1   # this algorithm ends up making low>high, which breaks out of the while loop


y = find_integer_sqaure(12)
print(y)
