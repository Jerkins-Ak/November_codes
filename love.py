'''
# Ask user for their name
name = input("Please enter your name: ")

# Define the correct name
correct_name = "Blessing" #,"Esblaug"x  # Replace with the actual correct name

# Check if the name is correct
if name == correct_name:
    for _ in range(10):
        print("I love you")
	time(0.5s)
else:
    print("Name is incorrect")
'''

import time

# Ask user for their name
name = input("Please enter your name: ")

# Define the correct name
#correct_name =( "Bea", "Blessing", "Esblaug")  # Replace with the actual correct name

# Check if the name is correct
#for name in correct_name:
if name == "Blessing":
	for _ in range(10):
		print("I love you")
		time.sleep(0.5)  # Wait for 0.5 seconds before printing the next line
elif name == "Bea":
	for _ in range(10):
		print("I love you")
		time.sleep(0.5)
elif name == "Candilicious":
	for _ in range(10):
		print("I love you")
		time.sleep(0.5)
elif name == "Esblaug":
	for _ in range(10):
		print("I love you")
		time.sleep(0.5)
else:
    print("Name is incorrect")
