#WordIndex.py
#Name: Nidhi Agarwal
#Date: 02/26/2026
#Assignment: Word Index lab

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary
  linenum = 0

  for line in textFile:
    linenum += 1
    wordlist = line.split()
    for w in wordlist:
      w= w.lower()
      w= w.replace("," ,  "")
      w= w.replace("." ,  "")
      w= w.replace("!" ,  "")
      
      if w in words:
        if linenum not in words[w]:
          words[w].append(linenum)
      else:
        words[w] = [linenum]  

    for word in words:
      print(word, words[word])

if __name__ == '__main__':
  main()
