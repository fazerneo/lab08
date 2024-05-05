# lab08
week 8 python lab

Exercises:

1. Write a function div that takes two numbers as parameters and returns the quotient of the first number divided by the second number. Use an try-except statement to do the division. In case of division by 0, use the except clause to return a special float value 'nan' (not a number).

Design a number of test cases to test the function (unit test) with the aim of identifying all possible errors of the function. For each test, specify both the input and the expected output. For each test case, carry out the test and compare the actual test result with the expected result.

2. Revise Exercise 1 in Lab 7: this time, your program must catch FileNotFoundError.

3. Revise Exercise 2 in Lab 7: this time, you must catch the following errors:

the file foo.txt doesn't exist.
the file bar.txt already exists.
Note: you should use try-except statement with multiple except clauses to catch and handle each of the errors.

4. Revise Exercise 4 in Lab 7: this time, you must check whether each staff record from the csv file has a staff id. If a staff record from the file doesn't have a staff id. Raise an Exception.

In your program, you should catch FileNotFoundError as well as the exception your program raised due to missing staff id. If the staff id is missing from the record, the whole record is ignored.

5. Revise Exercise 8 in Lab 4. This time, the function should use an assert statement to ensure that the parameter n is an integer in the range of 1 and 9 (inclusive). If this parameter is out of range, the assert statement should raise an exception.

Design a number of test cases to test whether the program meets the specification. Perform the tests and compare the expected results with the actual results. Your test programs should catch the exception thrown from the function.
