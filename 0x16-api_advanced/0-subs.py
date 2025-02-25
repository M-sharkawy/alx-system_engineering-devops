#!/usr/bin/python3
'''fetch the subscriber of subreddit'''

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "Users-Agent": "linux:0x16.api.advanced:v1.0.0"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")

    return 0
