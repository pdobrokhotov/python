'''
Unit Tests and Test Cases
The module unittest from the Python standard library provides tools for
testing your code. A unit test verifies that one specific aspect of a function’s
behavior is correct. A test case is a collection of unit tests that together prove
that a function behaves as it’s supposed to, within the full range of situations
you expect it to handle. A good test case considers all the possible
kinds of input a function could receive and includes tests to represent each
of these situations. A test case with full coverage includes a full range of unit
tests covering all the possible ways you can use a function. Achieving full
coverage on a large project can be daunting. It’s often good enough to write
tests for your code’s critical behaviors and then aim for full coverage only if
the project starts to see widespread use.
-------------------------------------------------------------
Table 11-1: Assert Methods Available from the unittest Module
-------------------------------------------------------------
assertEqual(a, b)          Verify that a == b
assertNotEqual(a, b)       Verify that a != b
assertTrue(x)              Verify that x is True
assertFalse(x)             Verify that x is False
assertIn(item, list)       Verify that item is in list
assertNotIn(item, list)    Verify that item is not in list
------------------------------------------------------------
'''
import unittest # We'll use this lib to test functionality of imported function below
from my_funct_module import get_formatted_name
#=====================================================================================
print("================================================================================")

class NamesTestCase(unittest.TestCase):
    """
    Tests for 'get_formatted_name' in file [my_funct_module.py].
    Any method that starts with test_ will be run automatically when we
    run test_name_function.py. 
    """
    def test_first_last_name(self): # Do names like 'Janis Joplin' work? 
        '''
        Within this test method, we call the function
        we want to test and store a return value that we're interested in testing. 
        In this example we call get_formatted_name() with the arguments 'janis' and 'joplin', 
        and store the result in formatted_name
        '''
        formatted_name = get_formatted_name('janis', 'joplin')
        ''' 
        Below we use one of unittest's most useful features: an assert method.
        Assert methods verify that a result you received matches the result you
        expected to receive. In this case, because we know get_formatted_name() 
        is supposed to return a capitalized, properly spaced full name, we expect
        the value in formatted_name to be Janis Joplin. To check if this is true, we
        use unittest's assertEqual() method and pass it formatted_name and 'Janis Joplin'. 
        The line below says: "Compare the value in formatted_name to the string 'Janis Joplin'.
        If they are equal as expected, fine. But if they don't match, let me know!"       
        '''
        self.assertEqual(formatted_name, 'Janis Joplin') 
    def test_first_last_middle_name(self): # Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
# After running command below (if all is fine) we'se on screen smth like:
#   Ran 1 test in 0.000s
#   OK    
# Otherwise we'll se error mesage explaining the difference in the actual and expected result    
unittest.main()
# Now we know that our function works OK for both cases with\without middle name
#=========================== NOTE ==========================================================
#When a test case is running, Python prints one character for each unit test as it is
#completed. A passing test prints a dot, a test that results in an error prints an E, and
#a test that results in a failed assertion prints an F. This is why you’ll see a different
#number of dots and characters on the first line of output when you run your test cases.
#If a test case takes a long time to run because it contains many unit tests, you can
#watch these results to get a sense of how many tests are passing.
#===========================================================================================



'''
#=======================================================================================
#=====================  TESTING FUNCTION OLD WAY  ======================================
print("================================================================================")
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
'''
