import time
import os

import requests
from twitterati import query_params
import dateutil.parser as parser

bearer_token = os.environ.get('BEARER_TOKEN')
headers = {"Authorization": "Bearer {}".format(bearer_token)}

def count_recent_tweets(search_query, granularity='day', start_time=None, end_time=None) -> dict:
    url = "https://api.twitter.com/2/tweets/counts/recent"
    if start_time:
       start_time = parser.parse(start_time).isoformat()
    if end_time:
        end_time = parser.parse(end_time).isoformat()

    params = {'query': search_query,
              'granularity': granularity,
              'start_time': start_time,
              'end_time': end_time}
    return requests.request("GET", url, headers=headers, params=params).json()


def recent_search_lookup(search_query, period, max_count = 5000) -> dict:
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = query_params.get_recent_search_query_params(search_query, period)
    all_responses = []
    response = requests.request("GET", url, headers=headers, params = params).json()
    all_responses.extend(response['data'])
    
    while 'next_token' in response['meta'] and len(all_responses) < max_count:
        params['next_token'] = response['meta']['next_token']
        response = requests.request("GET", url, headers=headers, params = params).json()
        all_responses.extend(response['data'])
    return all_responses

def conversation_lookup(conversation_id, timeout=2) -> dict:
    params = query_params.get_conversation_query_params(conversation_id)
    url = 'https://api.twitter.com/2/tweets/search/recent'
    results = requests.request("GET", url, headers=headers, params=params).json()
    time.sleep(timeout)
    if results['meta']['result_count'] == 0:
        return
    new_results = results.copy()
    while 'next_token' in new_results['meta']:
        params['next_token'] = new_results['meta']['next_token']
        new_results = requests.request("GET", url, headers=headers, params=params).json()
        results['data'].extend(new_results['data'])
        results['includes']['users'].extend(new_results['includes']['users'])
        if 'tweets' in new_results['includes']:
            results['includes']['tweets'].extend(new_results['includes']['tweets'])
        time.sleep(timeout)
    return results

def tweet_lookup(tweet_id, timeout=2) -> dict:
    url = 'https://api.twitter.com/2/tweets/{}'.format(tweet_id)
    params = query_params.get_tweet_query_params()
    time.sleep(timeout)
    return requests.request("GET", url, headers=headers, params=params).json()


def get_user_profile(user_id, update = False, timeout=6):
    url = "https://api.twitter.com/2/users/{}".format(user_id)    
    params = query_params.get_user_query_params()
    response = requests.request("GET", url, headers=headers, params = params).json()
    return response


def followers_lookup(user_id):
    url = "https://api.twitter.com/2/users/{}/followers".format(user_id)
    params = query_params.get_followers_query_params()

    all_responses = []
    response = requests.request("GET", url, headers=headers, params = params).json()
    all_responses.append(response)
    time.sleep(60)
    while 'next_token' in response['meta']:
        next_token = response['meta']['next_token']
        query_params['pagination_token'] = next_token
        response = requests.request("GET", url, headers=headers, params = params).json()
        all_responses.append(response)
        time.sleep(60)

    return all_responses

