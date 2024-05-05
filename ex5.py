def triangle_maker(num):
    ''' This function takes a single integer parameter and creates an right trangle
    out of it by repeating the integer in an increasing frequency in each iteration. This function also
    checks to see if the param is in a specific range. '''
    try:
        assert num in range(1,10), "num should be in the range 1 and 9(inclusive)"
        for i in range(1, num + 1):
            j = 0
            while j < i:
                print(num, end = "")
                j += 1
            print() 
        return
    except AssertionError as error:
        print(error)
        

''' _________TestCases_________'''

# Case 1: Normal Parameter. num in range 1 and 9(inclusive). Normal triangle expected
triangle_maker(9)
triangle_maker(1)
# Expected result == Actual result

# Case 2: num > 9. "num should be in the range 1 and 9(inclusive)" expected
triangle_maker(10)
# Expected result == Actual result

