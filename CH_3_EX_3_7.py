dinner_gusset = ['erica', 'alexis', 'mando', 'yoda', 'stan lee']
dinner_gusset.append('ducky')

message = f'Heloo, {dinner_gusset[0].title()} would you care to join me for dinner this evening?'
message_1 = f'Heloo, {dinner_gusset[1].title()} would you care to join me for dinner this evening?'
message_2 = f'Heloo, {dinner_gusset[2].title()} would you care to join me for dinner this evening?'
message_3 = f'Heloo, {dinner_gusset[3].title()} would you care to join me for dinner this evening?'
message_4 = f'Heloo, {dinner_gusset[4].title()} would you care to join me for dinner this evening?'

print(message)
print(message_1)
print(message_2)
print(message_3)
print(message_4)
popped_dinner_gusset = dinner_gusset.pop(3)
message_5 = f'unforchentily {popped_dinner_gusset} is unable to make it but we will be joined by {dinner_gusset[4]}'

print(message_5)
message_6 = f'Heloo, {dinner_gusset[4].title()} would you care to join me for dinner this evening?'
print(message_6)

dinner_gusset.insert(0, 'tony')
dinner_gusset.insert(5, 'fred')
dinner_gusset.append('sam')
message_7 = f'Heloo, {dinner_gusset[0].title()} would you care to join me for dinner this evening?'
print(message_7)
message_8 = f'Heloo, {dinner_gusset[5].title()} would you care to join me for dinner this evening?'
print(message_8)
message_9 = f'Heloo, {dinner_gusset[7].title()} would you care to join me for dinner this evening?'
print(message_9)

message_10 = 'Unfortunately the diner table will be unavailable in time, so I will only be able to invite two people to the party.'
print(message_10)

dinner_gusset_0 = dinner_gusset.pop(0)
message_11 = f'{dinner_gusset_0.title()} you are uninvited'
print(message_11)
dinner_gusset_1 = dinner_gusset.pop(2)
message_12 = f'{dinner_gusset_1.title()} you are uninvited'
print(message_12)
dinner_gusset_2 = dinner_gusset.pop(2)
message_13 = f'{dinner_gusset_2.title()} you are uninvited'
print(message_13)
dinner_gusset_3 = dinner_gusset.pop(2)
message_14 =f'{dinner_gusset_3.title()} you are uninvited'
print(message_14)
dinner_gusset_4 = dinner_gusset.pop(2)
message_15 = f'{dinner_gusset_4.title()} you are uninvited'
print(message_15)
dinner_gusset_5 = dinner_gusset.pop(2)
message_16 = f'{dinner_gusset_5.title()} you are uninvited'
print(message_16)
message_17 = f'{dinner_gusset[0]} you are still invited to dinner.'
print(message_17)
del dinner_gusset[0]
message_18 = f'{dinner_gusset[0]} you are still invited to dinner.'
print(message_18)
del dinner_gusset[0]
print(dinner_gusset)