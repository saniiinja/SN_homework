
import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0
wrong_guesses = []

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

    # get only the top 3 results
    score_list.sort(key=lambda x: x["attempts"])
    score_list = score_list[0:3]

    for score_dict in score_list:
        print(
            str(score_dict.get("attempts")) +
            " attempts, date: " + score_dict.get("date") +
            ", player: " + score_dict.get("player") +
            ", secret number: " + str(score_dict.get("secret_number"))
        )

player = input("Enter your name: ")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:

        score_list.append({
            "attempts": attempts,
            "date": str(datetime.datetime.now()),
            "player": player,
            "secret_number": secret,
            "wrong_guesses": wrong_guesses #add unsuccessful guesses into the dictionary
        })

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list, indent="\t")) #pretty printing indenting

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    else:
        wrong_guesses.append(guess)
        if guess > secret:
            print("Your guess is not correct... try something smaller")
        else:
            print("Your guess is not correct... try something bigger")


