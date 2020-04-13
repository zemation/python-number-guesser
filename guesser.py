#!/usr/local/bin/python3.7
import random


print('************************************')
print('**********Guess The Number**********')
print('************************************')
print()

random_number = random.randrange(1, 21)

def get_user_guess():
  user_guess = int(input('Guess a number between 1 and 20 (q to quit): '))
  return user_guess

def qualify_guess(guess):
  if guess == 'q':
    exit()
  elif (guess <= 0) or (guess > 20):
    qualify_guess(guess)
  else:
    return guess

qualify_guess(get_user_guess())


"""  elif (guess <= 0) or (guess > 20):
    return 'Please enter a number between 1 and 20'
  else:
    return determine_number(guess) 

def determine_number(guess):
  while guess != random_number:
    if user_guess > guess


while user_guess != random_number:
  if user_guess <= 0 or user_guess
  if user_guess > random_number:
    print('Your guess is too high.')
  elif user_guess < random_number:
    print('Your guess is too low.')
else: 
  print(f'You guessed correctly with the number {random_number}.')
"""


