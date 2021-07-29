import random

def get_guess():
    return list(input('What is your guess? '))

def generate_number():
    x = random.randint(100,999)

    return x

def generate_clue(code, guess):
    if code == guess:
        return 'CODE CRACKED!'

    clues = []

    for i,x in enumerate(guess):
        if x == code[i]:
            clues.append('match')
        else:
            clues.append('close')

    if clues == []:
        return ["Nope"]
    else:
        return clues

print("Welcome to Code Breaker! Let's see if you can guess my 3 digit number")
print('Code has been generated, please guess my 3 digit number')
x = int(input('What is your guess? '))
secret_code = generate_number()
clue_report = []

while clue_report != 'CODE CRACKED!':
    guess = get_guess()
    clue = generate_clue(secret_code, guess)
    print('Here is the result of your guess')
    for i in clue_report:
        print(clue)
