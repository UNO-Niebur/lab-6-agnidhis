#DiceRoll.py
#Name: Nidhi Agarwal  
#Date: 02/26/2026
#Assignment: Dice Roll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  trials = 10000
  #Create two dice values ranging from 1 - 6 each
  for r in range(trials):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    #find the sum total of the two dice
    total = dice1+dice2
    rolls[total-1] = rolls[total-1] + 1 

  #print statictics for dice rolls
  print("Total\tCount\tPercentage")
  for total in range(2,13) :
    count = rolls[total-1]
    percentage = (count/trials)*100
    decimal = round(percentage,2)
    print(f"{total} \t{count}\t{decimal}%")


if __name__ == '__main__':
  main()
