from cmath import nan


def div(num1, num2):
    ''' The function takes two numbers as parameters and returns the quotient of num2 divided by num2'''
    try:
        quotient = num1 / num2
        return quotient
    except ZeroDivisionError:
        return float(nan)
    except:
        return "Please pass valid parameters"
    
''' _________TestCases_________'''

# Case 1: Normal Parameters: num1 is 4 and num2 is 2, expected quotient is 2
print(f"Case 1: {div(4,2)}")
# Expected result == Actual result

# Case 2: num1 is bigger than num2, significantly small quotient expected. num1 is 2 and num2 is 40,000
print(f"Case 2: {div(2,40000)}") 
# Expected result == Actual result

# Case 3: num1 is equal to num2, quotient is 1 expected. num1 is 2, num2 is 2
print(f"Case 3: {div(2,2)}")
# Expected result == Actual result

# Case 4: num1 is a number and num2 is zero. nan expected. num1 is 2, num2 is 0
print(f"Case 4: {div(2,0)}")
# Expected result == Actual result

# Case 5: num1 is negative, num2 is negative. positive quotient expected. num1 is -2, num2 is -4
print(f"Case 5: {div(-2,-4)}")
# Expected result == Actual result

# Case 6: num1 is negative, num2 is positive. negative quotient expected. num1 is -4, num2 is 2
print(f"Case 6: {div(-4,2)}")
# Expected result == Actual result

# Case 7: num1 is positive, num2 is negative. negative quotient expected. num1 is 4, num2 is -2
print(f"Case 7: {div(4,-2)}")
# Expected result == Actual result

# Case 8: num1 is 0, num1 is positive. 0 is expected as quotient. num1 is 0, num2 is 1
print(f"Case 8: {div(0,1)}")
# Expected result == Actual result

# Case 9: num1 is 0, num2 is negative. 0 is expected as quotient. num1 is 0, num2 is -2
print(f"Case 8: {div(0,-2)}")
# Expected result != Actual result. Actual result was -0.0, which is not correct.

# Case 10: either or both number is float. normal quotient. num1 is 2.0, num2 is 4.0. num1 is 3.0, num2 is 2. num1 is 4, num2 is 2.0
print(f"Case 10.1: {div(2.0,4.0)}")
print(f"Case 10.2: {div(3.0,2)}")
print(f"Case 10.3: {div(4,2.0)}")
# Expected result == Actual result

# Case 11: String in either or both params. "Please pass valid parameters" expected. num1 is str, num2 is 2. num1 is str, num is str. numq is 4, num2 is str
print(f"Case 10.1: {div("rehar",2)}")
print(f"Case 10.2: {div("python","lab")}")
print(f"Case 10.3: {div(4,"murdoch")}")
# Expected result == Actual result