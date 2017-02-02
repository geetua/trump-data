#!/usr/bin/env python
"""
Downloads a timeline via Twitter's API

This requires a Twitter dev account and application with Consumer Key and
Secret
"""
import argparse
import requests
import base64
import os
import time
import sys
import json

def get_oauth_token(consumer_key, consumer_secret):
    """
    Gets an OAuth Bearer token as discussed here.

    See: https://dev.twitter.com/oauth/application-only

    consumer_key : Consumer Key (API Key) under Application Settings
    consumer_secret : Consumer Secret (API Secret) under Application Settings
    """
    auth = base64.b64encode('{}:{}'.format(consumer_key, consumer_secret))
    url = 'https://api.twitter.com/oauth2/token'
    data = 'grant_type=client_credentials'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization': 'Basic {}'.format(auth)
    }

    print >> sys.stderr, 'POST {}'.format(url)
    return requests.post(url, data=data, headers=headers).json()['access_token']

def get_timeline(user, oauth_token, count=100, max_id=None, since_id=None):
    """
    Retrieves the timeline for a given user.

    user : User name (without the leading @)
    oauth_token : Retrieved via get_oauth_token
    count : The number of timeline entries to retrieve in one request
    max_id : Sets max_id in the request; Tweets will be lower than this
    since_id : Sets since_id in the request; Tweets will be higher than this
    """
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}'.format(user, count)

    if max_id and not since_id:
        url += '&max_id={}'.format(max_id)
    elif since_id and not max_id:
        url += '&since_id={}'.format(since_id)
    elif max_id and since_id:
        raise Exception('Must only provide one of max_id or since_id')

    headers = {
        'Authorization': 'Bearer {}'.format(oauth_token)
    }

    print >> sys.stderr, 'GET {}'.format(url)
    return requests.get(url, headers=headers).json()

def get_id_from_timeline(timeline, fn):
    """
    Applies a function (like min / max) to IDs in timeline.
    """
    return reduce(fn, map(lambda x: x['id'], timeline))

def bootstrap(user, oauth_token, start_id=None):
    """
    Gets all Tweets starting at start_id until the beginning.
    """
    full = []
    last_id = start_id

    while True:
        timeline = get_timeline(user, oauth_token, max_id=last_id)
        full.extend(timeline)

        min_id = get_id_from_timeline(timeline, min)
        if last_id == min_id: break
        last_id = min_id

        time.sleep(1)

    return full

def poll(user, oauth_token, start_id=None):
    """
    Polls for new tweets from start_id at a 5s interval.
    """
    last_id=start_id
    while True:
        timeline = get_timeline(user, oauth_token, since_id=last_id)
        if len(timeline) > 0:
            for tweet in timeline:
                print json.dumps(tweet)
            last_id = get_id_from_timeline(timeline, max)
        time.sleep(5)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download tweets from a timeline')
    parser.add_argument(
        '--user',
        default='Trump_Regrets',
        help='Twitter handle (without the @)')
    parser.add_argument(
        '--bootstrap',
        action='store_true',
        default=False,
        help='Bootstrap back in time using max_id; otherwise, keep polling with since_id')
    parser.add_argument(
        'start_id',
        default=None,
        nargs='?',
        help='The start ID for the process')
    args = parser.parse_args()

    oauth_token = get_oauth_token(
        os.environ['CONSUMER_KEY'],
        os.environ['CONSUMER_SECRET'])

    if args.bootstrap:
        print >> sys.stderr, 'Bootstrapping {}'.format(args.user)
        data = bootstrap(args.user, oauth_token, args.start_id)
        print json.dumps(data)
    else:
        print >> sys.stderr, 'Polling for {}'.format(args.user)
        poll(args.user, oauth_token, args.start_id)
