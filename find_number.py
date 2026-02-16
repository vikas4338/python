import random
number_of_attempts = 0

mode = input("Enter mode 'easy' or 'hard ")

if mode == 'easy':
    number_of_attempts = 10
elif mode == 'hard':
    number_of_attempts = 5

number_to_guess = random.randint(1, 100)

for attempt in range(1, number_of_attempts + 1):
    user_guess = int(input("Guess the number "))
    if user_guess == number_to_guess:
        print("You got it")
        break
    elif user_guess > number_to_guess:
        print("Too High")
        print(f"You are left with {number_of_attempts - attempt} attempts")
    elif user_guess < number_to_guess:
        print("Too low")
        if(number_of_attempts != attempt):
            print(f"You are left with {number_of_attempts - attempt} attempts")
        else:
            print(f"You lost!!, number was {number_to_guess}")
