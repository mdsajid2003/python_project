import random
p = ['confess',"don't confess"]
pc = p[0]
pdc = p[1]
choice1 = str(random.choice(p))
choice2 = str(random.choice(p))
# print(type(choice2))
print(f'player1 {choice1} \nplayer2 {choice2}')
if choice1==pc and choice2 == pc:
    print(f"Both will get get 5 year imprisonment")
elif choice1 == pc and choice2 == pdc:
    print("player1 will be saved and player2 will get 10 years of imprisonment")
elif choice1 == pdc and choice2 == pc:
    print("player1 will be get 10 years of imprisoment and player2 will get saved")
else:
    print("both will get 1 years of imprisonment")