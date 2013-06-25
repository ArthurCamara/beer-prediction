#!/usr/bin/python

def main():
  f = open("top100.txt", 'r')
  words = []
  i=1
  for line in f:
    
    if i<50:
      words.append(line)
      i+=1
      continue
    linep = line.split()[0].rstip
    print linep
    linep = linep+"\n"
    words.append(linep)
    i+=1
  f.close()
  f = open("top100.txt", 'w')
  for w in words:
    print w
    f.write(w)
main()
