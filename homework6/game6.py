import random
import json
import datetime


class Result:
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = date


def get_score_list(top_score):
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())

        if top_score:
            score_list.sort(key=lambda x: x["attempts"])
            score_list = score_list[0:3]

        for score_dict in score_list:
            print(
                str(score_dict.get("attempts")) +
                " attempts, date: " + score_dict.get("date") +
                ", player: " + score_dict.get("player") +
                ", secret number: " + str(score_dict.get("secret_number"))
            )


def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = []

    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())

    player = input("Enter your name: ")
    level = input("Choose difficulty (easy, hard): ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:

            latest_result = Result(score=attempts,
                                   player_name=player,
                                   date=str(datetime.datetime.now())
                                   )
            score_list.append(latest_result.__dict__)

            """
            score_list.append({
                "attempts": attempts,
                "date": str(datetime.datetime.now()),
                "player": player,
                "secret_number": secret,
                "wrong_guesses": wrong_guesses
            })
"""
            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list, indent="\t"))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        else:
            wrong_guesses.append(guess)
            if level == "easy":
                if guess > secret:
                    print("Your guess is not correct... try something smaller")
                else:
                    print("Your guess is not correct... try something bigger")
            else:
                print("Your guess is not correct. Try again.")


while True:
    selection = input("Would you like to a) play a new game, b) see all scores, c) see the best scores, or d) quit? ")

    if selection == "a":
        play_game()
    elif selection == "b":
        get_score_list(False)
    elif selection == "c":
        get_score_list(True)
    else:
        print("\nGoodbye!")
        break
