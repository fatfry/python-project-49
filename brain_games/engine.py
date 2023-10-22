import prompt
from brain_games.consts import MAX_ATTEMPTS


def start_game(get_question_and_answer, instruction):
    name = prompt.string('Welcome to the Brain Games!/nMay I have your name?')
    print(f'Hello, {name}\n{instruction}')
    for _ in range(MAX_ATTEMPTS):
        question, result = get_question_and_answer()
        print(f'Question: {question}')
        user_input = prompt.string('Your answer:')
        if result == user_input:
            print('Correct!')
        else:
            print(f"'{user_input}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
