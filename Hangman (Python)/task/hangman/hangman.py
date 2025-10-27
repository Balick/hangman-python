import random
import string

words = ["python", "java", "swift", "javascript"]
success_nb, lost_nb = 0, 0


def get_user_input(guessed_letters):
    while True:
        print("\n" + "".join(guessed_letters))
        entry = input("Input a letter: ").strip()

        if len(entry) != 1:
            print("Please, input a single letter.")
        elif entry not in string.ascii_lowercase:
            print("Please, enter a lowercase letter from the English alphabet.")
        else:
            break
    return entry


def play():
    remaining_attempts = 8
    secret_word = random.choice(words)
    guessed_letters = ['-'] * len(secret_word)
    fake_guessed_letters = set()
    remaining_letters = list(secret_word)

    while remaining_attempts != 0:
        user_input = get_user_input(guessed_letters)

        if user_input in remaining_letters:
            indexes = [idx for idx, value in enumerate(secret_word) if value == user_input]

            for _, idx in enumerate(indexes):
                remaining_letters.remove(user_input)
                guessed_letters[idx] = user_input

            if secret_word == "".join(guessed_letters):
                print(f"You guessed the word {secret_word}!")
                return secret_word
        elif user_input not in remaining_letters and user_input in secret_word or user_input in fake_guessed_letters:
            print("You've already guessed this letter.")
        else:
            print("That letter doesn't appear in the word.")
            fake_guessed_letters.add(user_input)
            remaining_attempts -= 1

    return ''

print("H A N G M A N")

while True:
    menu = (input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
            .strip()
            .lower())

    if menu == "play":
        result = play()
        if result:
            success_nb += 1
            print("You survived!")
        else:
            lost_nb += 1
            print("\nYou lost!")
    elif menu == "results":
        print(f"You won: {success_nb} times.")
        print(f"You lost: {lost_nb} times.")
    elif menu == "exit":
        break
    else:
        pass
