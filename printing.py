import sys
import pprint
from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title

file_name = "game_stat.txt"
year = 2004
genre = "First-person shooter"
title = 'Counter-Strike'

a = count_games(file_name)
b = decide(file_name, year)
c = get_latest(file_name)
d = count_by_genre(file_name, genre)
e = get_line_number_by_title(file_name, title)

answers_for_Judy = [a, b, c, d, e]

pprint.pprint(answers_for_Judy) 