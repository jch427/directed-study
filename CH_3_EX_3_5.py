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

message_5 = f'unforchentily {dinner_gusset[3]} is unable to make it but we will be joined by {dinner_gusset[4]}'
print(message_5)
message_6 = f'Heloo, {dinner_gusset[4].title()} would you care to join me for dinner this evening?'
print(message_6)