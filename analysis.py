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
    countDict = dict()
    for review in user[u]['text']:
      text = re.findall(r"[\w']+", review)
      for word in text:
        if len(word)>=3:
          countDict[word] = countDict.get(word, 0) +1
          geralCount[word] = geralCount.get(word, 0)+1
  sorted_dict = sorted(geralCount.iteritems(), key=operator.itemgetter(1))
  print sorted_dict
  sorted_dict = sorted_dict.reverse()
  for i in range(100):
    print sorted_dict[i]
main()
