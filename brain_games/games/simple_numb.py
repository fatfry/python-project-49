import prompt
from random import randint


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def brain_prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is prime, otherwise answer 'no'.")
    count_win = 0
    while count_win < 3:
        number = randint(1, 100)
        print(f"Question: {number}")
        user_input = prompt.string("Your answer: ")
        result = is_prime(number)
        if result:
            result = "yes"
        else:
            result = "no"
        if result == user_input:
            print("Correct!")
            count_win += 1
        else:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
