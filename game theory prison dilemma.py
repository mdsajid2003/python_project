import random
print(f'=>Welcome to the game theory prison dilemma!!!<= \n' 
      ' There are some rules to be followed\n'
      ' 1) If you and your opponent confess then both of you end up in jail for 5 years jail \n'
      ' 2) If you confess and your opponent don"t he will end up in jail for 10 years and you will be saved \n' 
      " 3) If your opponent confess and you don't then you will end up in jail for 10 years and he will be saved \n"
      ' 4) If both of you do not confess then both are saved')
choice1 = input(" Enter either you want to confess or don't confess \n")
p = ['confess',"don't confess"]
pc = p[0]
pdc = p[1]
# choice1 = str(random.choice(p))
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
    print("both will be saved years of imprisonment")
