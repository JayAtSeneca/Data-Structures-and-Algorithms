def wins_rock_scissors_paper(arg1, arg2):
    if (arg1.upper() == "ROCK" and arg2.upper() == "SCISSORS") or (arg1.upper() == "PAPER" and arg2.upper() == "ROCK") or (arg1.upper() == "SCISSORS" and arg2.upper() == "PAPER"):
        return True
    else:
        return False

# print(wins_rock_scissors_paper("rock","scissors"))
# print(wins_rock_scissors_paper("rock","paper"))
# print(wins_rock_scissors_paper("scissors".upper(),"paper"))
# print(wins_rock_scissors_paper("Scissors","Rock"))
# print(wins_rock_scissors_paper("paper","sCiSsOrs"))
# print(wins_rock_scissors_paper("paper".title(),"ROCK"))
# print(wins_rock_scissors_paper("paper","PaPeR"))
# print(wins_rock_scissors_paper("rock","ROCK"))
# print(wins_rock_scissors_paper("SCISSORS","scissors"))