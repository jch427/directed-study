bicycles = ['trek', 'cannondle', 'redline', 'specialized'] # 0 indicates the first position in the list
print(bicycles[0].title())                                 # in the () the [] indicates witch thing in the list should be printed. change the 0 to 1-3 for a diferent listr iteam.
                                                           # can add .title and other such modifiers to the output.
print(bicycles[1])                                         # accessing element in position 1. the second on in the list.
print(bicycles[3])                                         # accessing element in position 3. the forth on in the list.
print(bicycles[-1])                                        # -1 always returns the last element in the list. - numbers start from 1 and go up from the bottem of the list.
message = f"my first bicycle was a {bicycles[0].title()}." #what dose the "f" do?
print(message)
