import unittest # We'll use this lib to test functionality of imported CLASS below
from my_class_module import AnonymousSurvey
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
We start by importing the unittest module and the class we want to
test, AnonymousSurvey. We call our test case TestAnonymousSurvey, which again
inherits from unittest.TestCase. The first test method will verify that
when we store a response to the survey question, the response ends up in
the survey’s list of responses. A good descriptive name for this method is
test_store_single_response() v. If this test fails, we’ll know from the method
name shown in the output of the failing test that there was a problem storing
a single response to the survey.
'''
#=========================================================
# Tests for the class AnonymousSurvey 
class TestAnonmyousSurvey(unittest.TestCase):
    def test_store_single_response(self): # Test that a single response is stored properly. 
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    #---------------------------------------------------------------------------------------
    def test_store_multi_responses(self): # Test that three individual responses are stored properly.
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses: # store all responses to a Class
            my_survey.store_response(response)
        for response in responses: # verify that current response is really stored in Class
            self.assertIn(response, my_survey.responses)
#===========================================================================================
#Begin testing and assert that all is fine
unittest.main() #Run 2 tests for single\multiple responses
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
print("===============  TESTING CLASS OLD WAY  =========================================")
#=======================================================================================
# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if  response == 'q':
        break
    my_survey.store_response(response)
# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
#=====================================================================================
'''