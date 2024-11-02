#!/bin/bash

echo "Welcome!"
echo "Enter Details to register"

read -p "Enter Username: " name
read -p "Enter password: " pass

echo "Successfully registered!!!"
echo "Enter details to login"

read -pm"Enter Username: " u_name
if [u_name eq name]; do
	echo "Correct username"

else;
	echo "Incorrect username"
fi


read -pm"Enter password: " p_word
if [u_name eq name]; do
	echo "Correct username"

else;
	echo "Incorrect username"
fi

