#!/usr/bin/python
# coding=utf-8

import pickle
import re
import operator

def main():
  SW = []
  SW_F = open('stopwords', 'r')
  out_f = open('top100.txt', 'w')
  for w in SW_F:
    SW.append(w.rstrip('\n'))
  print SW
  print "loading users"
  geralCount = dict()
  user = pickle.load(open("users.pkl", 'rb'))
  print "done"
  for u in user:
    for review in user[u]['text']:
      text = re.findall(r"[\w']+", review)
      for word in text:
        if len(word)>=3 and (word.upper() not in SW):
          geralCount[word.upper()] = geralCount.get(word.upper(), 0)+1
  sorted_dict = sorted(geralCount.iteritems(), key=operator.itemgetter(1))
  for i in reversed(range(len(geralCount)-101, len(geralCount))):
    print sorted_dict[i]
    out_f.write(str(sorted_dict[i][0]) + '\n')
main()
