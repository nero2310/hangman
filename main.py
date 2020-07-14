import random


def letter_positions(secret_word, guess):
    positions = []
    counter = 0
    for i in secret_word:
        if i == guess:
            positions.append(counter)
        counter += 1
    return positions

def load_word_from_file():
    with open("slownik.txt", "r") as file:
        lines = file.readlines()
    word = random.choice(lines)
    return word




def word_encryption(word):
    cryptogram = list()
    for i in word.lstrip().rstrip():
        if i == " ":
            cryptogram += " "
        else:
            cryptogram += "_"
    return cryptogram


def menu(attempts=3):
    print("""1.Enter a word 
2.Get random word from file""",end="")
    guess = input(":")
    if guess == "1":
        word = input("Enter a word :")
    elif guess == "2":
        word = load_word_from_file()
    secret_word = word_encryption(word.lstrip().rstrip())
    for i in range(0, attempts):
        print(''.join(secret_word))
        guess = input("Guess a letter :").lstrip()
        positions = letter_positions(word, guess)
        if len(positions) == 0:
            attempts -= 1
        for letter_position in positions:
            secret_word[letter_position] = guess
        if secret_word.count("_") == 0:
            print("Congratulations")
            print(''.join(secret_word))
            break


if __name__ == "__main__":
    menu(20)
