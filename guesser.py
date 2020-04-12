#!/usr/local/bin/python3.7
import random


print('************************************')
print('**********Guess The Number**********')
print('************************************')
print()

random_number = random.randrange(1, 21)
user_guess = ''

while user_guess != random_number:
  user_guess = int(input('Guess a number between 1 and 20: '))
  if user_guess > random_number:
    print('Your guess is too high.')
  elif user_guess < random_number:
    print('Your guess is too low.')
else: 
  print(f'You guessed correctly with the number {random_number}.')
