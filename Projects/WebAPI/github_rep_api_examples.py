import requests
#===========================================================
# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# A status code of 200 indicates a successful response.
print("Status code:", r.status_code)
#-----------------------------------------------------------
# Store API response in a variable.
# The API returns the information in JSON format,
response_dict = r.json()

# Process results. 
'''
The dictionary.keys() method returns a list of all the keys 
in the dictionary in order of insertion. In below code this 
list will be like: ['total_count', 'incomplete_results', 'items']
'''
print(response_dict.keys()) # = ['total_count', 'incomplete_results', 'items']
print("Total repositories:", response_dict['total_count']) # = 9009827
# Explore information about the repositories.
# Store this list of dictionaries in repo_dicts.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts)) # = 30
#=====================================================================
# Examine the first repository.Store the first item from repo_dicts  
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict)) # = Keys: 79
for key in sorted(repo_dict.keys()):
    print(key)

#====================================================
print("\n\n=============================================")
print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
#-------------------------------------------------------
# An entire dictionary represents the project’s owner, 
# so we use the key owner to access the dictionary 
# representing the owner and then use the key login  
# to get the owner's login name. ("owner" is dectionary itself)
print('Owner:', repo_dict['owner']['login'])
#-------------------------------------------------------
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])
'''                    RESULT 
Selected information about first repository:
Name: Python-100-Days
Owner: jackfrued
Stars: 126192
Repository: https://github.com/jackfrued/Python-100-Days
Created: 2018-03-01T16:05:52Z
Updated: 2022-10-12T16:34:37Z
Description: Python - 100天从新手到大师
'''
#======================================================= 
# Summarizing the Top Repositories. Loop through all the
# dictionaries in repo_dicts. Inside the loop we print 
# the name of each project,its owner, how many stars it 
# has, its URL on GitHub, and the project's description:
print("\n\n=============================================")
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])



