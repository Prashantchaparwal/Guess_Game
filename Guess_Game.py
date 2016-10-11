import time
print("Welcome to the world of Games.") # To print.
print("")
while(1):   # For users who would like to play again.
	time.sleep(3)       #To provide Pause after 2 sec.
	name = input("Enter Your Name: ")
	print("")
	time.sleep(3)
	print("Hello  " +name, ", this is a game of Guess")
	print("")
	time.sleep(3)
	while(1):   # for users who have entered a wrong value.
		print("Guess a Number between 1 to 10")
		time.sleep(3)
		print("")
		print("Multiply the number you have guessed by 2 ")
		time.sleep(3)
		print("")
		print("Add 2 to the answer ")
		time.sleep(3)
		print("")
		print("Multiply the answer by 5 ")
		time.sleep(3)
		print("")
		print("Add 5 to the answer ")
		time.sleep(3)
		print("")
		print("Multiply the answer by 10 ")
		time.sleep(3)
		print("")
		print("Add 10 to the answer ")
		time.sleep(3)
		print("")
		print("")
		while(1):            # It would repeat again if the answer is not yes.
			Calc = input("Are you done with the Calculations?  yes Or no.")    #input from user to continue.
			print("")
			if(Calc.lower() == "yes"):
				num1 = int(input("Enter The number calculated"))
				print("")
				break;
			if(Calc.lower() == "no"): 
				print("Do your calculations fast......")
				print("")
			if(Calc.lower() != "yes") and (Calc.lower() != "no" ):
				print("That option is not available......")	
				print("")
	#def Valid():
		if num1%100 == 60:
			print("")
			print("Your answer is being processed")
			time.sleep(3)
			print("")
			result = int(num1/100-1)
			print("The Number you had Guessed Was :" + str(result))
			print("")
			print("Hope you loved the Magic....!!!!!!!")
			print("")
			break;
		else:
			print("Your Going Wrong Somwhere")
			print("")
			print("Lets Give 1 more Go:")
			print("")
	while(1):    # this while is used if the user is not entering the right choice to play again.
		ch = input("Would You Like To play Again? yes or no")
		print("")
		if(ch.lower() == "yes"):
			print("")
			break;
		if(ch.lower() == "no"): 
			print("Thank you for playing....")
			exit();
		if(ch.lower() != "yes") and (Calc.lower() != "no" ):
			print("That option is not available......")	
			print("")
