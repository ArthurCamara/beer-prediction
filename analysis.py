#!/usr/bin/python
# coding=utf-8

import pickle
import re
import operator

def main():
  print "loading users"
  geralCount = dict()
  user = pickle.load(open("users.pkl", 'rb'))
  print "done"
  for u in user:
    for review in user[u]['text']:
      text = re.findall(r"[\w']+", review)
      for word in text:
        if len(word)>=3:
          geralCount[word.upper()] = geralCount.get(word.upper(), 0)+1
  sorted_dict = sorted(geralCount.iteritems(), key=operator.itemgetter(1))
  for i in reversed(range(len(geralCount)-101, len(geralCount))):
    print sorted_dict[i]
main()
