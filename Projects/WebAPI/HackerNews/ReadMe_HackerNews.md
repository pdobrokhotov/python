                       The Hacker News API
To explore how you would use API calls on other sites, we’ll look at Hacker
News (http://news.ycombinator.com/). On Hacker News people share articles
about programming and technology, and engage in lively discussions about
those articles. Hacker News’ API provides access to data about all submissions
and comments on the site, which is available without having to register
for a key. The following call returns information about the current top article as of this writing:
https://hacker-news.firebaseio.com/v0/item/9884165.json
The response is a dictionary of information about the article with the ID 9884165:

{
'url': 'http://www.bbc.co.uk/news/science-environment-33524589',
'type': 'story',
'title': 'New Horizons: Nasa spacecraft speeds past Pluto',
'descendants': 141,
'score': 230,
'time': 1436875181,
'text': '',
'by': 'nns',
'id': 9884165,
'kids': [9884723, 9885099, 9884789, 9885604, 9885844]
}

The dictionary contains a number of keys we can work with, 
such as 'url' and 'title'. The key 'descendants' contains 
the number of comments an article has received. The key 'kids'
provides the IDs of all comments made directly in response to 
this submission. Each of these comments may have kids of their 
own as well, so the number of descendants a submission has can
be greater than its number of kids.