#!/usr/bin/env python
import argparse
import urllib2

parser = argparse.ArgumentParser()
parser.add_argument('url' ,type = str, help = 'web address')
args = parser.parse_args()
url = args.url
def download(url):
    return urllib2.urlopen(url).read()
