# Attempt at making dice roller program
# Still need to implement exception handling
# Still need to implement a loop for the moreinfo variables
import random
from statistics import mean

# Allows for multiple modes
def mode(ls):
    # dictionary to keep count of each value
    counts = {}
    # iterate through the list
    for item in ls:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    # get the keys with the max counts
    return [key for key in counts.keys() if counts[key] == max(counts.values())]


berapaDice = int(input("How many dice would you like to roll? "))
if berapaDice <= 0:
    berapaDice = int(input("Bruh for real tho: "))
sided = int(input("How many sides are on each die? "))
if sided <= 0:
    sided = int(input("Bruh come on give me a normal choice: "))
dicelist = list(range(berapaDice))
dicelist[0] = 1                                    #Useful if dice values are set to 1 and then multiplied, I guess
results = (random.choices(range(1,sided), k = berapaDice))
if berapaDice <= 100:
    print("Your dice values are: " + str(results))
else:
    print("Since you wanted to roll more than 100 dice, I'm not gonna print them.")
average = mean(results)
moded = mode(results)
modeamount = results.count(moded[0])
#print(results)
stats = print("The average value of your rolls was " + str(average) +
              ", and the number(s) which showed up most frequently was/were " + str(moded) +
              ", which appeared " + str(modeamount) + " times!")
#print(moded)
requestedno = int(input("Which number do you want info on? "))
moreinfo = results.count(requestedno)
print("The number " + str(requestedno) + " showed up " + str(moreinfo) + " times.")
