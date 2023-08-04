import prompt


def start_game(get_question_and_answer, instruction):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(instruction)
    for i in range(3):
        question, result = get_question_and_answer()
        print(f'Question: {question}')
        user_input = prompt.string('Your answer: ')
        if result == user_input:
            print('Correct!')
        else:
            print(f"\'{user_input}\' is wrong answer ;(. Correct answer was \'{result}\'.\nLet's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
