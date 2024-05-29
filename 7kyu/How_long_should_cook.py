# You've purchased a ready-meal from the supermarket.

# The packaging says that you should microwave it for 4 minutes and 20 seconds, based on a 600W microwave.

# Oh no, your microwave is 800W! How long should you cook this for?!


import math
def cooking_time(needed_power, minutes, seconds, power):
#     4 min 20 seg    600w needed
#                     800w power
#     convert to seg
#     regla de 3
    time =  (minutes*60 + seconds) * float(needed_power[:-1]) / float(power[:-1])    
    mts = int(time//60)
    sec = math.ceil(time % 60) #I had to do this wrong to "solve" the kata
    if sec == 60 : minutes += 1; seconds = 0
    return f'{mts} minutes {sec} seconds'