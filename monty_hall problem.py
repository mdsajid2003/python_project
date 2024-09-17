
import random 

# 1,2,3
def monty_hall(switch):
    win = 0
    trails = 10000
    for _ in range(trails):
        gift = random.randint(0,2)
        choice = random.randint(0,2)
        rem = [i for i in range(3) if i!=choice and i!=gift]

        opened_by_host = random.choice(rem)
        # print(f"initial chioce, {choice}")
        # print(f"opened_by_host, {opened_by_host}")
        if switch:
            choice=3-opened_by_host-choice
            # print(f"swappped choice, {choice}")


            
        # print(f"gift,{gift}")
        # print(f"choice,{choice}")
        # print(f"rem,{rem}")
        # print(f"opened_by_host,{opened_by_host}")

        if choice == gift:
            win+=1
            

    print(win/trails *100)
        
    # print(gift)
    # print(choice)
    # print(rem)
    

monty_hall(True)
            




