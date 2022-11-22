import json


class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.2046
        return pounds

#nasljeđuje klasu Player
class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


first_name = input("Enter player's first name: ")
last_name = input("Enter player's last name: ")
height = input("Enter player's height: ")
weight = input("Enter player's weight: ")
points = input("Number of points: ")
rebounds = input("Number of rebounds: ")
assists = input("Number of assists: ")

new_player = BasketballPlayer(first_name=first_name,
                              last_name=last_name,
                              height_cm=float(height),
                              weight_kg=float(weight),
                              points=float(points),
                              rebounds=float(rebounds),
                              assists=float(assists)
                            )

with open("basketball_players.json", "r") as basketball_file:
    basketball_players = json.loads(basketball_file.read())

    basketball_players.append(new_player.__dict__)

with open("basketball_players.json", "w") as basketball_file:
    basketball_file.write(json.dumps(basketball_players))

print("Player successfully entered!")
print("Player's data: {0}".format(new_player.__dict__))
