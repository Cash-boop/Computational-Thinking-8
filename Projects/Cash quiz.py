Arsenal = 0
Man_city = 0
Tottenham = 0 
Chelsea = 0 
# question 1:
answer = input("Whats your favorite color A) Red, B) Blue, C) Navy, D) White?\n")
if answer == "A":
	Arsenal += 1
elif answer == "B":
	Man_city += 1
elif answer == "C":
	Chelsea += 1 
elif answer == "D":
	Tottenham += 1 
	
answer = input("What would you want to do with your friends A) Just chill, B) Steal, C) Play date, D) You have no freinds?\n")
if answer == "A":
	Arsenal += 1
elif answer == "B":
	Man_city += 1
elif answer == "C":
	Chelsea += 1 
elif answer == "D":
	Tottenham += 1 
	
answer = input("Whats your favorite food A) Steak, B) Robbery, C) Candy, D) Salad?\n")
if answer == "A":
	Arsenal += 1
elif answer == "B":
	Man_city += 1
elif answer == "C":
	Chelsea += 1 
elif answer == "D":
	Tottenham += 1 
	
answer = input("How old are you A) Above 25, B) Under 10, C) Under 5, D) Over 80?\n")
if answer == "A":
	Arsenal += 1
elif answer == "B":
	Man_city += 1
elif answer == "C":
	Chelsea += 1 
elif answer == "D":
	Tottenham += 1 
	
answer = input("Whats your favorite chant A) What do you think of totenham, B) Blue moon, C) Cocomelon, D) Come on you spurs?\n")
if answer == "A":
	Arsenal += 1
elif answer == "B":
	Man_city += 1
elif answer == "C":
	Chelsea += 1 
elif answer == "D":
	Tottenham += 1 
	
answer = input("Would you pay the refs as a manager A) No, B) Yes, C) Idk, D) Dont have enough money?\n")
if answer == "A":
	Arsenal += 1
elif answer == "B":
	Man_city += 1
elif answer == "C":
	Chelsea += 1 
elif answer == "D":
	Tottenham += 1 
	
answer = input("Whats your favorite animal A) Gorrila, B) Mermaid, C) Lion, D) Chicken on a beachball?\n")
if answer == "A":
	Arsenal += 1
elif answer == "B":
	Man_city += 1
elif answer == "C":
	Chelsea += 1 
elif answer == "D":
	Tottenham += 1 
	
answer = input("How many trophies has your team one A) too many to count, B) 10, C) 2, D) Zero?\n")
if answer == "A":
	Arsenal += 1
elif answer == "B":
	Man_city += 1
elif answer == "C":
	Chelsea += 1 
elif answer == "D":
	Tottenham += 1 
	
answer = input("Favorte influencer A) Andrew tate, B) David Goggins, C) Dillon Lathem , D) Jake paul?\n")
if answer == "A":
	Arsenal += 1
elif answer == "B":
	Man_city += 1
elif answer == "C":
	Chelsea += 1 
elif answer == "D":
	Tottenham += 1 
	
answer = input("What place is your favorite pl team A) 2, B) 5, C) 4, D) pretty much last ?\n")
if answer == "A":
	Arsenal += 1
elif answer == "B":
	Man_city += 1
elif answer == "C":
	Chelsea += 1 
elif answer == "D":
	Tottenham += 1 
	

if Arsenal > Tottenham:
	print("You are a Arsenal fan")
elif Arsenal >= Chelsea:
	print("You are a Arsenal fan")
elif Arsenal >= Man_city:
	print("You are a Arsenal fan")
elif Arsenal <= Man_city:
	print("You are a Man city fan")
elif Tottenham <= Man_city:
	print("You are a Man city fan")
elif Chelsea <= Man_city:
	print("You are a Man city fan")
elif Arsenal <= Chelsea:
	print("You are a Chelsea fan")
elif Man_city <= Chelsea:
	print("You are a Chelsea fan")
elif Tottenham <= Chelsea:
	print("You are a Chelsea fan")
elif Tottenham >= Chelsea:
	print("You are a Tottenham fan")
elif Tottenham >= Man_city:
	print("You are a Tottenham fan")
elif Tottenham >= Arsenal:
	print("You are a Tottenham fan")
	

	
