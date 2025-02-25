#!/usr/bin/python3
'''recursive function that queries the Reddit API'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return the list recersively"""
    url =  f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {
        "Users-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        for posts in data['children']:
            hot_list.append(posts.get("data").get("title"))
        if not after:
            return hot_list
        return (recurse(subreddit, hot_list, after))
    return None
