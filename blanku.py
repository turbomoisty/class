#!/usr/bin/env python3
import random
# Shorcut to comment multiple lines: command + /
#

# while True:
#
# temp = input("Would you like to convert to Celsius or Fahrenheit -> ")
#
# if temp.lower() == "c":
#	 fahreheit = float(input("Enter the Fahrenheit value: "))
#	 answer = (fahreheit - 32) * (5/9)
#	 print("Celsius value: " + "{:.2f}".format(answer))
#	 break
#
# elif temp.lower() == "f":
#	 celcius = float(input("Enter the Celsius value: "))
#	 answer = (celcius * (9/5) + 32)
#	 print("Fahrenheit value: " + "{:.2f}".format(answer))
#	 break
#
# else:
#	 print("Invalid input, pick 'c' or 'f'.")

# number = input("Enter four digits ->")
#
# array_sum = sum(int(total) for total in (str(number)))
#
# print(array_sum)

# fruits =int(input("Enter the numbers you would like the sum of: "))
# fruit_list = []
# for i in range(fruits):
#
#	entry = int(input(f"Enter Entry {i + 1}: "))
#	fruit_list.append(entry)
#	answer = sum(fruit_list)
#	print(answer)

# age = int(input("Enter your age -> "))
#
# if age < 12:
#	print("Your price is $5.")
#
# elif age >= 12 and age <= 18:
#	print("Your price is $7.")
#
# elif age > 18:
#	print("Your price us $12")
#
# else:
#	print("You are too old or too young.")
#


# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
#
# name1_count = name1.lower()
# name2_count = name2.lower()
#
# true_word = ['t','r','u','e']
# love_word = ['l','o','v','e']
#
# true_count = 0
# love_count = 0
#
# for true_char in true_word:
#	true_count += name1_count.count(true_char) + name2_count.count(true_char)
#
# score = int(true_count)
#
# print(f"{score}")

# while True:
#	print("Welcome to treasure island. Your mission is to find the treasure.")
#
#	direction = input("Would you like to go left or right? -> ").lower()
#	if direction == "right":
#		option = input("You have died. Start over? ->").lower()
#		if option == "yes":
#			continue
#		elif option == "no":
#			break
#
#	elif direction =="left":
#		option2 = input("You come across a river. Swim or wait -> ").lower()
#		if option2 == "swim":
#			gameover = input("You drowned. Game over. Start again? -> ").lower()
#			if gameover == "yes":
#				continue
#			else:
#				break
#		elif option2 == "wait":
#			option3 = input("You spot a boat not far off the distance. After rowing to the other side, you spot a building with two doors. Which door will you enter? -> ").lower()
#			if option3 == "red":
#				gameover = input("You died. Try again? yes - no").lower()
#				if gameover == "yes":
#					continue
#				else:
#					break
#			elif option3 == "yellow":
#				print("You win!")
#				break

#	else:
#		print("Unknown input.")
#		break
#

# def remove_exMark(f):
#	return f.replace("a", "").replace("e","")
#
#
# remover = input("Enter any sentence -> ")
#
# answer = remove_exMark(remover)
#
# print(answer)

# def bmi(weight, height):
##
##	BMI = (float(weight / (height **2)))
##
##	return ["Underweight","Normal","Overweight","Obese"][(BMI <= 18.5) + (BMI <= 2) + (BMI >= 30) + (BMI >= 35)]
##
##
##result = bmi(55,4)
##
###print(result)
# def get_volume_of_cuboid(length, width, height):
#	# Code goes here...
#
#	return (length * width * height)
#
# length = int(input("Enter length"))
# width = int(input("Enter width"))
# height = int(input("Enter height"))
# volume = get_volume_of_cuboid(length, width,height)
# gofakks the volume
# print(volume)


##function called find_needle with (haystack) as argument
# def find_needle(haystack):
#
## The index function searches from the list 'haystack' and  gives the position of the string "needle" into the variable 'needle'
#	needle = haystack.index("needle")
#	print(f'found the needle at position {needle}')
## list called find_needle containing elements
# needles = find_needle(["efefs","srgshjbfse","needle"])
#
# lambda_example = lambda x,b : x + b / 12
#
# print(int(lambda_example(3,8)))
##
# def some_examples(arr):
#
#	#----initialise two variables to keep count of positive and negative sums
#	positive_sum = 0
#	negative_sum = 0
#	positive_count = 0
#
#	#---- if arr has no value, return null
#	if not arr: return []
#	#----initialise a for loop for the parameter arr in some_examples
#	for num in arr:
#		#-----if num in the arr is greater than 0, iterate the positive_sum by adding the num values..
#		if num > 0:
#			positive_sum += num
#			#-----if num in the arr is greater than 0, iterate the positive_sum value by one.
#			positive_count +=1
#			if num < 0:
#				negative_sum += num
#
#				return [positive_count,positive_sum,negative_sum]
#
#			#----Create a variable and make a list
# original_list = [1, -2, 3, -4, 5]
#
##----create another variable and declare original_list as the argment for some_examples
# example_list = some_examples(original_list)
#
# print(example_list)
#

# first_name = input("first name - ")
# second_name = input("second name - ")
#
# f_name_lower = first_name.lower()
# s_name_lower = second_name.lower()
#
#
#
# true_word = ['t','r','u','e']
# love_word = ['l','o','v','e']
#
# true_count = 0
# love_count = 0
#
# for t_word in true_word:
#	true_count += f_name_lower.count(t_word) + s_name_lower.count(t_word)
#
# for l_word in love_word:
#	love_count += f_name_lower.count(l_word) + s_name_lower.count(l_word)
#
# true_love_count = str(true_count) + str(love_count)
#
# int_TL = int(true_love_count)
#
# print(int_TL)

# the .strip() method  removes any leading or trailing whitespace from the input. If there is a argument in the method, it will splice from there
# .title() Still capitalise the first letter of any string input
# name = input("What is your name: ").strip().title()
#
# first, last = name.split("d")
#
# print(f"Hello {name}")
# formatted_string = f"{x:.2f}"

# x_list = [2,6,3,7,4,89,45]
#
# list_over_12 = 0
# sum_over_7 = 0
#
# for number in x_list:
#	if number > 2:
#		list_over_12 += 1
#
#	if number > 7:
#		sum_over_7 += number
#
# print(list_over_12, sum(x_list), sum_over_7)

# moist_amount = int(input("enter amount: "))
#
# while True:
#	if moist_amount < 0:
#		int(input("Enter a valid number: "))
#
#	else:
#			print("moist\n" * moist_amount, end="")
##			break
#
#
#


# def main():
#	x = int(input("Enter a value: "))
# print(value_of_x(x))
#
# def value_of_x(y):
#	return y * 5
#
# main()
#

# car_list = [
#	{"Brand" : "Audi", "Year" : "1992", "Model" : "A4"},
#	{"Brand" : "Toyota", "Year" : "2019", "Model" : "Yaris"},
#	{"Brand" : "Honda", "Year" : "2003", "Model" : "Integra"}
# ]
#
# for cars in car_list():
#	print( cars["Year"],cars["Model"], sep = " ")

# def main():
#		is_even = int(input("Enter number: "))
#		if modulo(is_even) == 0:
#			print(True)
#		else:
#			print(False)
#
#
# def modulo(is_even):
#	return bool(is_even % 2)
#
# main()

# input_string = input("Enter numbers")
#
# test1,test2,test3 = map(float,input_string.split(","))
#
# print(test1,test2,test3 )


#
# while True:
#	try:
#		num_cookies = int(input("Enter the number of biscuits: "))
#		if num_cookies < 0:
#			print("Enter value above 0")
#			continue
#		break
#
#	except ValueError:
#		print("Enter a valid input")
#
# dozen_num = int(num_cookies / 12)
# dozen_value = dozen_num * 5
# remainder = int(num_cookies % 12)
# remainder_value = remainder * 0.5
#
# total_value = dozen_value + remainder_value
#
# print(f"You have ordered {num_cookies} cookies , that's {dozen_num} dozen and {remainder} cookies. The total cost is ${total_value}.")


# my_list = []
#
# list_size = int(input("Enter list size: "))
#
# for i in range(1,list_size + 1):
#	element = input(f"Enter element {i}")
#	my_list.append(element)
#
# print(my_list)

# def main():
#	hash_printer(3)
#
# def hash_printer(num_hashes):
#	# for each x axis/row in num_hashes
#	for x in range(num_hashes):
#		# for each y axis/column in row
#		for y in range(num_hashes):
#			print("o",end="")
#		print()
#
#
# main()

# def main():
#	hash_printer(3)
#
# def hash_printer(num_hashes):
#	for x in range(num_hashes):
#		print("o" * num_hashes)
#
#
# main()

# def main():
#     x = get_int()
#     print(f"x is {x}")
#
# def get_int():
#     while True:
#         try:
#             return int(input("Value of x: "))
#         except ValueError:
#             pass
#
# main()
# from random import choice # from the random module, select the 'choice' method
# from random import randint # same as before but select the 'randint' method
#
# coin = ["heads","tails"]
# choices = choice(coin)
# print(choices)
# start = 1
# end = 9
# rand_value = randint(start,end) # random ini method takes two arguments, and randomly chooses a number between the two values
# # in this instance it will pick a number between 1 and 3 inclusive.
# true_word = ['t','r','u','e']
# letter_gen = choice(true_word)
#
# cards = ['spade','heart','clover','diamond']
# random.shuffle(cards)
#  #shuffles the list order from cards, then prints the card
# print(cards)
#
# print(letter_gen)
# print(rand_value)

# random.choice(["heads", "tails"])


# import statistics
#
# def main():
#     scores = get_score()
#     print(statistics.mean(scores))
# def get_score():
#     scores_list = []
#     scores_count = 1
#
#     print("Enter the scores values. type 'end' to stop entering scores ")
#     while True:
#
#         scores_values = input(f"Enter the value for position {scores_count}: ")
#         scores_list.append(scores_values)
#         scores_count += 1
#
#         if scores_values == "end":
#             del scores_list[-1]
#             return [int(scores_values) for scores_values in scores_list]
#
# main()


# def main():
#     x = get_int("what is x: ")
#     print(f"x is {x}")
#
# def get_int(prompt):
#     while True:
#         try:
#             x = int(input(prompt))
#         except ValueError:
#             pass
# main()


# def main():
#	import sys
#
#	username = "John"
#	password = "doe"
#	user_id = 123
#
#	password_attempts = 0
#	while True:
#		username_login = input("Enter username: ")
#		password_login = input("Enter password: ")
#		try:
#			user_id_login = int(input("Enter your user id: "))
#
#		except ValueError:
#			print("Enter a valid user id.Try again")
#			continue
#
#
#		if username_login != username and password_login != password and user_id_login != user_id:
#			print("One of your login details are wrong. Try again.")
#			password_attempts += 1
#			if password_attempts == 3:
#				print("Too many attempts have been made.")
#				sys.exit()
#
#		else:
#			print(f"User Login successful! Welcome {username}")
#			choice = int(input("Enter 1. Calculator\n 2. List\n "))
#			if choice == 1:
#				calculator()
#			if choice == 2:
#				list_creator()
#			break
#
#
#
# def calculator():
#
#	value_1 = input("Enter first value: ")
#	value_2 = input("Enter Second value: ")
#
#	choice = input("Enter '1' for addition")
#
#	if choice == '1':
#		print(addition(value_1, value_2))
#
# def addition(value_1, value_2):
#	return int(value_1) + int(value_2)
#
#
# def list_creator():
#
#	my_list = []
#
#	while True:
#		try:
#			list_size = int(input("Enter the size of the list:"))
#
#		except ValueError:
#			print("Input is not a valid number. Try again.")
#
#		else:
#
#			for _ in range(list_size):
#
#				numbers = int(input(f"Enter the values in for {_ + 1} in list: "))
#				my_list.append(list_size)
#
#		print(my_list)
#
#
# main()
#


# °C = (°F − 32) x 5/9
# °F = (°C × 9/5) + 32

import json
# import requests
#
# # using the slice function [1:] (or to take a subset of the data structure).
# name = input()
#
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + name)
#
# o = response.json() # stores the json response in a variable called "o"
# for result in o["results"]: #for results the onbject o, in the keyword called 'results'
#     print(result["trackName"]) #print out the result's trackname

import sys

import doppio  # from the filename 'doppio' import a function.


def main():
    x = int(input("x?: "))
    print(f"Answer is ", squared(x))


def squared(number):
    return number ** 2


if __name__ == "__main__":
    main()
