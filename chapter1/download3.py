#!/usr/bin/env python
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('url' ,type = str, help = 'web address')
args = parser.parse_args()
url = args.url
def download(url):
    response = requests.get(url)
    print(response.text)
    return response.text

if __name__ == '__main__':
    download(url)
