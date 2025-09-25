import random
is_playing = True

print("********** Welcome to the Rock Paper Scissors Game **********")
while is_playing:
    user_guess = input("Enter your choice (rock,paper,scissors): ").lower()
    computer_choice = random.choice(['rock','paper','scissors'])
    
    if user_guess == computer_choice:
        print(f"Both players selected {user_guess}. It's a tie!")
        print("Try again!")
        keep_playing = input("Do you want to play again? (yes/no): ").lower()
        if keep_playing == 'yes':
            print("Great! Let's play again.")
            continue
        
        else:
            print("Thanks for playing! Goodbye.")
            break
        
    else:
        if user_guess == 'rock' and computer_choice == 'scissors':
            print("Rock smashes scissors! You win!")
        elif user_guess == 'paper' and computer_choice == 'rock':
            print("Paper covers rock! You win!")
        elif user_guess == 'scissors' and computer_choice == 'paper':
            print("Scissors cuts paper! You win!")
        elif computer_choice == 'rock' and user_guess == 'scissors':
            print("Rock smashes scissors! You lose.")
        elif computer_choice == 'paper' and user_guess == 'rock':
            print("Paper covers rock! You lose.")
        elif computer_choice == 'scissors' and user_guess == 'paper':
            print("Scissors cuts paper! You lose.")
            
        is_playing = False
        print("Thanks for playing! Goodbye.")