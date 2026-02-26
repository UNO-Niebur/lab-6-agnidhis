#WordCount.py
#Name:Nidhi Agarwal
#Date:02/26/2026
#Assignment: Word Count 

def main():
  textFile = open("gettysberg.txt", 'r')
  linecount = 0
  wordcount = 0
  lettercount = 0

  for line in textFile:
   linecount  += 1
   wordcount  += len(line.split())
   lettercount += len(line)
  
  print("Lines: ", linecount)
  print("Words: ", wordcount)
  print("Characters: ", lettercount)

if __name__ == '__main__':
  main()
