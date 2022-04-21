import os
import argparse

import requests

from dotenv import load_dotenv
from urllib.parse import urlparse


URL_BITLINK = 'https://api-ssl.bitly.com/v4/'


def check_token_valid(headers):
    url = f'{URL_BITLINK}user'
    response = requests.get(
        url,
        headers=headers,
    )
    response.raise_for_status()


def is_bitlink(headers, netloc_path):
    url = f'{URL_BITLINK}bitlinks/{netloc_path}'
    response = requests.get(url, headers=headers)
    return response.ok


def check_url_accessibility(url):
    response = requests.get(url)
    response.raise_for_status()


def shorten_link(headers, url):
    payload = {
        'long_url': url,
        'domain': 'bit.ly',
    }
    response = requests.post(
        f'{URL_BITLINK}shorten',
        headers=headers,
        json=payload,
    )
    return response.json()['link']


def count_clicks(headers, netloc_path):
    payload = {
        'unit': 'day',
        'units': -1,
    }
    response = requests.get(
        f'{URL_BITLINK}bitlinks/{netloc_path}/clicks/summary',
        headers=headers,
        params=payload,
    )
    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    headers = {'Authorization': f'Bearer {token}'}
    check_token_valid(headers)
    parser = argparse.ArgumentParser(description='Shortens long url\
                                     \nor counts clicks on a bitlink.')
    parser.add_argument('url', help = 'Your link or bitlink')
    args = parser.parse_args()
    url = args.url
    check_url_accessibility(url)
    try:
        netloc_path = f'{urlparse(url).netloc}/{urlparse(url).path}'
        if is_bitlink(headers, netloc_path):
            clicks_count = count_clicks(headers, netloc_path)
            print('Number of clicks: ', clicks_count)
        else:
            bitlink = shorten_link(headers, url)
            print('Bitlink: ', bitlink)
    except requests.exceptions.HTTPError:
            print("Something's wrong with your url.\
                   \nCheck it and try again.")
