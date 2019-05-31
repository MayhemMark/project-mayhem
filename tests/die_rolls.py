import random


def roll_dice():
	list1 = []
	sides = int(input("how many sides does the die have?: "))
	times = int(input("how many times do you want to roll? "))
	print(f"\nRolling a {sides} sided die, rolling it {times} times")
	print("These are the results:\n")
	for i in range(0,times):
		list1.append(random.randint(1,sides))
		
	print(list1)
	print(f"the total of your rolls: {sum(list1)}")	
		
	pick = input("\nroll again? y/n: ")
	if pick == "y":
		roll_dice()
	else:
		return

		
			
roll_dice()
