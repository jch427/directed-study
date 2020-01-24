pizza = ['pepperoni', 'ham', 'BBQ']
friend_pizza = pizza[:]

pizza.append('neapolitan')
friend_pizza.append('margherita')
#for pizza in pizza:
    #print(f"{pizza} is one of my favorite types of pizza")
#print(f"pizza is one of the foods i could eat every day.")

print('My favorite pizzas are:')
for pizza in pizza:
    print(pizza)
print("My friends favorite pizzas are:")
for friend_pizza in friend_pizza:
    print(friend_pizza)