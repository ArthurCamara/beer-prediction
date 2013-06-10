#!/usr/bin/python
import pickle
import re

def countUser():
  print "loading users"
  users = pickle.load(open("users.pkl", 'rb'))
  print "done"
  for u in users:
    countDict = dict{}
    for review in users[u]['text']:
      text = re.findall(r"[\w']+", review)
      for word in text:
        countDict[word] = countDict.get(word, 0) +=1
    print countDict




