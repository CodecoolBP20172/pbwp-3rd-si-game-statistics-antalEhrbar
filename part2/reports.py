import sys
import math
genre = "RPG"
file_name = "game_stat.txt"
title = "Counter-Strike"
# Report functions


def get_most_played(file_name):
    line_in_gam_stat = 0
    latest_game_year = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as myfile:
        for line in myfile:
            results.append(line.strip().split('\t'))
    for i in results:
        if float(results[line_in_gam_stat][1]) > float(latest_game_year):
            latest_game_year = results[line_in_gam_stat][1]
            name_of_this_game = results[line_in_gam_stat][0]
        line_in_gam_stat += 1
    return(name_of_this_game)


def sum_sold(file_name):
    line_in_gam_stat = 0
    num_of_sold_games = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as myfile:
        for line in myfile:
            results.append(line.strip().split('\t'))
        for i in results:
            num_of_sold_games += float(results[line_in_gam_stat][1])
            line_in_gam_stat += 1
        return(num_of_sold_games)


def get_selling_avg(file_name):
    line_in_gam_stat = 0
    num_of_sold_games = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as myfile:
        for line in myfile:
            results.append(line.strip().split('\t'))
        for i in results:
            num_of_sold_games += float(results[line_in_gam_stat][1])
            line_in_gam_stat += 1
        return(num_of_sold_games/len(results))


def count_longest_title(file_name):
    len_of_title = 0
    line_in_gam_stat = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as myfile:
        for line in myfile:
            results.append(line.strip().split('\t'))
        for i in results:
            if len(results[line_in_gam_stat][0]) > len_of_title:
                len_of_title = len(results[line_in_gam_stat][0])
            line_in_gam_stat += 1
        return len_of_title


def get_date_avg(file_name):
    line_in_gam_stat = 0
    num_of_sold_games = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as myfile:
        for line in myfile:
            results.append(line.strip().split('\t'))
        for i in results:
            num_of_sold_games += float(results[line_in_gam_stat][2])
            line_in_gam_stat += 1
        return(math.ceil((num_of_sold_games/len(results))))


def get_game(file_name, title):
    x = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as myfile:
        for line in myfile:
            results.append(line.strip().split('\t'))
    for i in results:
        if results[x][0] == title:
            break
        x += 1
    results[x][1] = float(str(results[x][1]))
    results[x][2] = int(str(results[x][2]))
    return results[x]
