# Attempt at making dice roller program
# Still need to implement exception handling
import random

berapaDice = int(input("How many dice would you like to roll? "))
if berapaDice <= 0:
    berapaDice = int(input("Bruh be normal: "))
sided = int(input("How many sides are on each die? "))
if sided <= 0:
    sided = int(input("Bruh come on: "))
dicelist = list(range(berapaDice))
dicelist[0] = 1

print("Your dice values are: " + str(random.choices(range(1,sided), k = berapaDice)))
