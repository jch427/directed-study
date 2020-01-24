# how many iteams? 5
# how many messages? 5
# how many prints? 5
# are they all in the same message/print? no
car = ['tesla', 'ford', 'honda', 'GMC', 'doge']

message = f'the new {car[0].title()} truck is unlike any other befor it.'
message2 = f'comparied to the old{car[1].title()} F150 it is very interesting.'
message3 = f'unlike {car[1].title()}, {car[2].title()}, {car[3].title()}, {car[4].title()} the look is radicaly diferent.'
message4 = f'{car[0].title()} chose to go for a more futeristic look that reminds me of a video game truck.'
message5 = f'all the negative press i have seen for the new {car[0].title()} truck has been about how it looks but i do not see any of the other componys such as {car[1].title()} doing anything about it.'
print(message)
print(message2)
print(message3)
print(message4)
print(message5)
