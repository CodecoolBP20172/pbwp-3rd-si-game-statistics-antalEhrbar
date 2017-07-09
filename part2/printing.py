
# Printing functions
import sys
import pprint
from reports import get_most_played, sum_sold, get_selling_avg, count_longest_title, get_date_avg, get_game, count_grouped_by_genre

file_name = "game_stat.txt"
year = 2004
genre = "First-person shooter"
title = 'Counter-Strike'

a = get_most_played(file_name)
b = sum_sold(file_name)
c = get_selling_avg(file_name)
d = count_longest_title(file_name)
e = get_date_avg(file_name)
f = get_game(file_name, title)
g = count_grouped_by_genre(file_name, genre)

answers_for_Judy = [a, b, c, d, e, f, g]

pprint.pprint(answers_for_Judy) 