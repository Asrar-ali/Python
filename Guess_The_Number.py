import random

attempts=10

def num_checker(u_guess, random_n):
    if u_guess == rand_num:
        print(f"You got it! The answer was {rand_num}. ")
    elif u_guess > rand_num:
        print("Too High")
    elif u_guess < rand_num:
        print("Too Low")

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
u_choice=input("Choose a difficulty. Type 'easy' or 'hard' :").lower()

rand_num  = int(random.randint(0,100))

if u_choice=='easy':
    for i in range(0, 10):
        print(f"You have {attempts-i} attempts remaining to guess the number. ")
        guess = int(input("Make a guess: "))
        num_checker(guess, rand_num)
    print("You ran out of attempts you lost!.")
elif u_choice=='hard':
    for i in range(0, 5):
        print(f"You have {attempts/2-i} attempts remaining to guess the number. ")
        guess=int(input("Make a guess: "))
        num_checker(guess, rand_num)
    print("You ran out of attempts you lost!.")
