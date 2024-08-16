#!/usr/bin/python3
"""
File that contains recursive function that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as javascript,
but java should not).
"""
import requests


def count_words(subreddit, word_list, next_page=None, count=None):
    """
    Queries the Reddit API, parses the title of all hot articles, and
    prints a sorted count of given keywords
    (case-insensitive, delimited by spaces).
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'CUSTOM'}
    params = {'after': next_page}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return  # Invalid subreddit or no posts

    data = response.json()

    for post in data['data']['children']:
        title = post['data']['title']
        title_words = title.lower().split()

        for word in counts:
            counts[word] += title_words.count(word)

    after = data['data']['after']
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    else:
        # Print results
        sorted_counts = {k: v for k, v in counts.items() if v > 0}
        sorted_counts = sorted(sorted_counts.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_counts:
            print('{}: {}'.format(word, count))
