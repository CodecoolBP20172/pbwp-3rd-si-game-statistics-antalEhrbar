import sys
file_name = "game_stat.txt"
year = 2004
genre = 'First-person shooter'
title = 'Counter-Strike'


def count_games(file_name):
    results = []
    try:
        with open(sys.path[0] + '/' + file_name, "r") as myfile:
            results.append(sum(1 for line in myfile if line.rstrip('/n')))
    except FileNotFoundError:
        print("The file is missing.")
    return results[0]


def decide(file_name, year):
    results = []
    try:
        with open(sys.path[0] + '/' + file_name, "r") as myfile:
            for line in myfile:
                if str(year) in line:
                    return True
                else:
                    False
    except FileNotFoundError:
        print("The file is missing.")


def get_latest(file_name):
    just_a_variable = 0
    latest_game_year = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as myfile:
        for line in myfile:
            results.append(line.strip().split('\t'))
        for i in results:
            if int(results[just_a_variable][2]) > int(latest_game_year):
                latest_game_year = results[just_a_variable][2]
                name_of_this_game = results[just_a_variable][0]
            just_a_variable += 1
        return(name_of_this_game)


def count_by_genre(file_name, genre):
    numb_of_this_genre = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as myfile:
        for line in myfile:
            results.append(line.strip().split('\t'))
        for i in results:
            if genre in i:
                numb_of_this_genre += 1
        return numb_of_this_genre

def get_line_number_by_title(file_name, title):
    x = 0
    eredmenyek = []
    with open(sys.path[0] + '/' + file_name, "r") as myfile:
        for line in myfile:
            eredmenyek.append(line.strip().split('\t'))
    for i in eredmenyek:
        x += 1
        if title in i:
            break
        if x == 24:
            return "This game is not in this list ma'am"
    return x
