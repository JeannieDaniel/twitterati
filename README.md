# Why twitterati
We like to uncomplicate things, and wrappers (except when they actually wrap :gift ) do exactly that. 

This package serves as a wrapper for Twitter API V2 Early Access, for more info: https://developer.twitter.com/en/docs/twitter-api/early-access.

## What is new in Twitter API V2?
- Pick and choose which fields you want the API to return
- Advanced insights using annotations, which adds named entity tags to certain topics, such as (Barack Obama, PERSON)
- Filtered Streaming capabilities (not yet supported by twitterati)
- More expressive query languages

## Functions supported by twitterati 0.0.3:
- Tweet lookup by Tweet ID
- Whole conversation lookup by Conversation ID
- Recent search for query terms over past 7 days
- Count occurrences of query term over past 7 days
- User lookup by User ID
- Follows lookup by User ID

# Before you get started:

Be sure to familiarize yourself with the terms and conditions of the Twitter Developer API: https://developer.twitter.com/en/developer-terms/agreement-and-policy. 

Also, take note of the restricted use cases, detailed here: https://developer.twitter.com/en/developer-terms/more-on-restricted-use-cases 

You will need to register an account and an application to collect your Bearer token: https://developer.twitter.com/en/apply-for-access

Take note of the rate limits: the Standard Track limits the number of tweets you can collect to 500,000 per month. 

You must keep all API keys or other access credentials private. 

## Installation
```
pip3 install twitterati
```
## Credentials

Once allocated, you can export your bearer token to your environment:

```shell
export BEARER_TOKEN='XXXXXXXXXXX'
```


## Getting a user's metadata

```python

from twitterati import lookups

user = lookups.get_user_profile(user_id)

```

## Getting all the tweets that contain a search term over the past 7 days


```python

from twitterati import lookups

tweets = lookups.recent_search_lookup('python', max_count = 1000)

```


## Count the number of tweets that contain a search term over the past 7 days


```python

from twitterati import lookups

counts = lookups.count_recent_tweets('python')

```




## Getting a conversation by conversation_id:

```python

from twitterati import lookups

convo = lookups.conversation_lookup(conversation_id)

```
