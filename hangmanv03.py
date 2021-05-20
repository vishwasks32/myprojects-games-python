#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
# Script for hangman game version 0.1
import random

def load_words(fl_nme):
	try:
		fl_hndle = open(fl_nme,'r')
		f_names = list()
		for item in fl_hndle.readlines():
			f_names.append(item)
			
		return f_names
	except:
		return 0
	
def choose_word():
	fruit_words = load_words("fruit_names.txt")
	if fruit_words != 0:
		rdm_idx = int(random.randint(0,5))
		# Chosen Word
		return fruit_words[rdm_idx]
	else:
		return 0
	

if __name__ == '__main__':
	print("Enter to the game of HANGMAN")
	print("I Have chosen a word of a fruit")
	print("Note: You will lose chances for invalid inputs")
	word = choose_word()
	if word == 0 :
		print("Source File not found")
		exit(0)
	
	for i in word:
		print('_', end = ' ')
		
	print()
	playing = True
	guessed = ''
	guessed_word = ''
	chances = 7
	correct = 0

	while(chances != 0):
		print()
		chances -= 1
		guess = input("Enter a letter guess: ")
		if not guess.isalpha() or len(guess) > 1:
			print("Not a valid input, you lost a chance")
			
		elif guess in guessed:
			print("Already Guessed")
			
		else:
			#print("The guessed letter is: %s"%(guess))
			guess = guess.upper()
			guessed += guess
			guessed_word = ''
			print(guessed)
			for letter in word:
				if letter in guessed :
					guessed_word += letter
					print(letter, end = ' ')
				else:
					print('_', end = ' ')
				
			print()
			if guessed_word == word:
				print("You Won")
				break	
			elif chances == 0:
				print("You Lost")
			else:
				continue
