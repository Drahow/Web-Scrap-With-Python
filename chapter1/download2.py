#!/usr/bin/env python
import argparse
import urllib2

parser = argparse.ArgumentParser()
parser.add_argument('url' ,type = str, help = 'web address')
args = parser.parse_args()
url = args.url
def download(url):
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'download error: ', e
        html = None
    return html

if __name__ == '__main__':
    download()
