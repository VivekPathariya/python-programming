import random

#welcom message

print("Welcome to Rock - Paper - Scissors Game !")

User_score = 0

computer_score=0

while True:
    
    user_input = input("Choose :- 'rock' , 'paper' , 'scissors' : ").lower()
    
    if user_input not in ['rock','paper','scissors']:
        
        print("Incorrect Choice ! Please try again.")
        
        continue
    
    computer_choice = random.choice(['rock','paper','scissors'])
    
    print(f"\n You are chose:-{user_input}")
    
    print(f"Computer chose :- {computer_choice}")
    
    if user_input == computer_choice:
        
        print("It's a tie !")
        
    elif  (user_input== "rock"and computer_choice == "scissors")or\
          (user_input == "scissors"and computer_choice =="paper")or\
          (user_input == "paper"and computer_choice == "rock"):
              
          print(" Congretulation Your win!")
          
          User_score += 1
          
    else:
        
        print("Oops Sorry your lose !")
        
        computer_score += 1
        
    print(f"\n Scores :- You - {User_score} , Computer - {computer_score}")
    
    play_again = input("\n Do you want to play again ? (yes/no):-").lower()
    
    if play_again != "yes" :
        
        break
    
    print("\n Thank you for playing !") 
    
           
          
              
                    