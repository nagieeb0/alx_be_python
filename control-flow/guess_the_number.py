import random

# def guess_the_number():
#     #! GENERATE A SECRET NUMBER BETWEEN 1 AND 10
#     secret_number = random.randint(1, 10)

#     print("I'M THINKING OF A NUMBER BETWEEN 1 AND 10. CAN YOU GUESS IT?")

#     #! INITIALIZE THE COUNTER FOR THE NUMBER OF GUESSES
#     guess_count = 0

#     while True:
#         guess = int(input("ENTER YOUR GUESS: "))
    
#         #! INCREMENT THE GUESS COUNTER
#         guess_count += 1

#         #! MATCH THE USER'S GUESS WITH THE SECRET NUMBER
#         match guess:
#             case _ if guess == secret_number:
#                 print(f"CONGRATULATIONS, YOU GUESSED IT IN {guess_count} TRIES!")
#                 break  #! EXIT THE LOOP IF THE GUESS IS CORRECT
#             case _ if guess > secret_number:
#                 print("OOPS, YOUR GUESS IS A BIT HIGH. TRY AGAIN!")
#             case _ if guess < secret_number:
#                 print("NOPE, YOUR GUESS IS A BIT LOW. GIVE IT ANOTHER SHOT!")

#     #! PLAY AGAIN ??? 
#     play_again = input("PLAY AGAIN? (YES/NO): ").lower()

#     if play_again == "yes":
#         guess_the_number()  #! RESTART THE GAME
#     else:
#         print("THANKS FOR PLAYING! GOODBYE!")

# #! START THE GAME
# guess_the_number()


#_ print("Guessing Game!")

while True:  #! LOOP TO ALLOW REPLAYING THE GAME
    secret_number = random.randint(1, 10)
    guess_count = 0  #! Counter
    print("\nI'm thinking of a number between 1 and 10. Can you guess it?")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        guess_count += 1  #! INCREMENT THE GUESS COUNTER
        
        match guess:
            case _ if guess == secret_number:
                print(f"Congratulations, you guessed it in {guess_count} tries!")
                break #! IF CORRECT QUIT TO RESTART
            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
    
    #! PLAY AGAIN !!! 
    play_again = input("Play again? (yes/no): ")
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break