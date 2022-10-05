import unittest # We'll use this lib to test functionality of imported CLASS below
from my_class_module import AnonymousSurvey
'''
This testing is almost the same as in file [TESTING_CLASS.py]
but it uses additional method = def setUp(self):
The method setUp() does two things: it creates a survey instance u,
and it creates a list of responses v. Each of these is prefixed by self, so
they can be used anywhere in the class. This makes the two test methods
simpler, because neither one has to make a survey instance or a response.
The method test_store_single_response() verifies that the first response in
self.responses—self.responses[0]—can be stored correctly, and test_store_
single_response() verifies that all three responses in self.responses can be
stored correctly.
'''
#=========================================================
# Tests for the class AnonymousSurvey with SETUP-method
# NOTE: When we use "self"-prefix with variable, it means this variable can be accesed with CLASS
#       Also, methos "setUp(self)" works smth like "__init__"-method
class TestAnonmyousSurvey(unittest.TestCase):
    def setUp(self): # Create a survey and a set of responses for use in all test methods.
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    #---------------------------------------------------------------------------------------
    def test_store_single_response(self): # Test that a single response is stored properly. 
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    #---------------------------------------------------------------------------------------
    def test_store_multi_responses(self): # Test that three individual responses are stored properly.
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
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