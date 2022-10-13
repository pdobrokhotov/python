import requests
from operator import itemgetter
#=============================================================
# Make an API call and store the response and print its status
# This call returns a list containing the IDs of the 500 most 
# popular articles on Hacker News at the time the call is issued
# This will return us a list of IDs we need to look thru like: 
# [33187677,33188276,33185010,...]
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
# print("Status code:", r.status_code) # if =200 it's OK
#=============================================================
# Process information about each submission.
# Convert the response text to List where we store in submission_ids. 
# We’ll use these IDs to build a set of dictionaries that each store 
# information about one of the current submissions.
submission_ids = r.json() # read submission IDs to list-variable
#print ('===================== submission_ids ===================')
#print (submission_ids)
#print ('=========================================================')
submission_dicts = []     # create an empty list to fill in
#=============================================================
# Loop through the IDs of the top 30 submissions. We make a new
# API call for each submission by generating a URL that includes 
# the current value of submission_id
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission by creating dynamic URL
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)# get data from current Submision ID
    # print(submission_r.status_code) # if = 200, then call was OK
    # Save response for current Submision ID to list-variable
    response_dict = submission_r.json() # parse jason-respose and save it
    # Pull from current json-response the data we need: 'title','comments' etc
    # and save ut into dictioanary variable, that we'll appent to main LIST  
    submission_dict = {'title': response_dict['title'],
                       'link': 'http://news.ycombinator.com/item?id=' + 
                       str(submission_id),
                       'comments': response_dict.get('descendants', 0)
                       }
    '''
    Above we store the number of comments in the dictionary. If an article has 
    no comments yet, the key 'descendants' will not be present. When you're not 
    sure if a key exists in a dictionary, use the dict.get() method,which returns
    the value associated with the given key if it exists or the value you provide
    if the key doesn't exist (0 in this example).
    '''
    # Appent currently pulled dictionary variable 
    # to our main LIST of dictionaries 
    submission_dicts.append(submission_dict)
 
#=============================================================
# Sort our MAIN LIST 
submission_dicts = sorted(submission_dicts, 
                          key=itemgetter('comments'),
                          reverse=True)
'''
Above we sort the list of dictionaries by the number of comments. 
To do this, we use a function called itemgetter(), which comes
from the operator module. We pass this function the key 'comments', 
and it pulls the value associated with that key from each dictionary 
in the list. The sorted() function then uses this value as its basis 
for sorting the list. We sort the list in reverse order to place 
the most-commented stories first.
'''
#=============================================================
# Print three pieces of information about each of the top submissions: 
# the title,a link to the discussion page, and the number of comments 
# the submission currently has:
print('\n====================================================')
for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
    