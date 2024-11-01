#!/usr/bin/env python3

#A simple code to ask the user for name and password

print ("Welcome!!!")

name = input("Enter your username to register: ")
password = input("Enter password: ")

print ("Account created succesfully")
print ("Proceed and login")

name_check = input("Enter username to login: ")
#pass_check = input("Enter password: ")

if name_check == name:
    print ("Correct username")
else:
    print ("Unregistered user")


pass_check = input("Enter password: ")

if pass_check == password:
    print ("Welcomr")
else:
    print ("Wrong password")




