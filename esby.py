#!/usr/bin/env python3
'''
import time
print("Welcome to Jer Jer World")
esby = input ("Enter your name: ")
bby = ("Blessing", "Esblaug", "Esby", "Candilicious", "Jerkwins")
if  esby in bby:
	for _  in range (10):
		print ("I love you")
		time.sleep(0.5)
else :
	print("Go away you are not my bby")
'''

import time

print("Welcome to Jer Jer World")

# Ask user for their name
esby = input("Enter your name: ")

# Define the list of correct names
bby = ("Blessing", "Esblaug", "Esby", "Candilicious", "Jerkwins")

# Check if the name is in the list of correct names
if esby in bby:
    for _ in range(100):
        print(f"I love you {esby} , you mean the world and beyond to me")
        time.sleep(0.5)  # Wait for 0.5 seconds before printing the next line
else:
    print("Go away you are not my bby")
