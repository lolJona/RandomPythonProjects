# Attempt at making dice roller program
# Still need to implement exception handling
# Still need to implement a loop for the moreinfo variables
import random

berapaDice = int(input("How many dice would you like to roll? "))
if berapaDice <= 0:
    berapaDice = int(input("Bruh for real tho: "))
sided = int(input("How many sides are on each die? "))
if sided <= 0:
    sided = int(input("Bruh come on give me a normal choice: "))
dicelist = list(range(berapaDice))
dicelist[0] = 1                                    #Useful if dice values are set to 1 and then multiplied, I guess
results = (random.choices(range(1,sided), k = berapaDice))
print("Your dice values are: " + str(results))
#print(results)
requestedno = int(input("Which number do you want info on? "))
moreinfo = results.count(requestedno)
print("The number " + str(requestedno) + " showed up " + str(moreinfo) + " times.")
requestedno2 = int(input("Which other number do you want info on? "))
moreinfo2 = results.count(requestedno2)
print("The number " + str(requestedno2) + " showed up " + str(moreinfo2) + " times.")
