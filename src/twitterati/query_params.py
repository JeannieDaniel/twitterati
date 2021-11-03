import datetime
import pytz

def get_conversation_query_params(conversation_id, max_result=100):
    return  {'query': 'conversation_id:{}'.format(conversation_id),
            'tweet.fields': 'author_id,conversation_id,created_at,in_reply_to_user_id,lang,referenced_tweets',
            'user.fields': 'id,created_at,username,name,description,location,public_metrics,url,verified,entities',
            'expansions': 'author_id,in_reply_to_user_id,referenced_tweets.id',
            'max_results': max_result
            }

def get_tweet_query_params():
    return  {
            'tweet.fields': 'author_id,conversation_id,created_at,in_reply_to_user_id,lang,referenced_tweets',
            'user.fields': 'id,created_at,username,name,description,location,public_metrics,url,verified,entities',
            'expansions': 'author_id,in_reply_to_user_id,referenced_tweets.id',
            }

def get_followers_query_params(max_results = 100):
    return {'user.fields': 'id,created_at,username,name,description,location,public_metrics,url,verified,entities',
            'max_results':100}

def get_user_query_params():
    return {'user.fields':'id,created_at,username,name,description,location,public_metrics,url,verified,entities'}

def get_recent_search_query_params(search_query, period, max_results=100):

    # Calculate startdate if period is provided
    if period is not None:
        d = datetime.datetime.utcnow() + datetime.timedelta(days=-period)
        start_time = d.replace(tzinfo=pytz.UTC).isoformat()

        query_params = {
                            'query': search_query,
                            'user.fields': 'id,created_at,username,name,description,location,public_metrics,url,verified,entities',
                            'tweet.fields': 'author_id,in_reply_to_user_id,created_at,conversation_id,public_metrics,lang,geo,referenced_tweets,entities',
                            'expansions': 'author_id',
                            'max_results': max_results,
                            'start_time' : start_time,
                        }

        return query_params

    else:
        query_params = {
                            'query': search_query,
                            'user.fields': 'id,created_at,username,name,description,location,public_metrics,url,verified,entities',
                            'tweet.fields': 'author_id,in_reply_to_user_id,created_at,conversation_id,public_metrics,lang,geo,referenced_tweets,entities',
                            'expansions': 'author_id',
                            'max_results': max_results
                        }

        return query_params