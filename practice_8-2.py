from random import randint
turns = 0 # 遊戲次數
easy_turns = 10
hard_turns = 5

def set_difficulty():
   global turns
   level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
   if level == "easy":
       turns = easy_turns
   else:
       turns = hard_turns

def check_answer(user_guess, actual_answer):
   if user_guess > actual_answer:
       print("Too hight.")
       return False
   elif user_guess < actual_answer:
       print("Too low.")
       return False
   else:
       print(f"You got it! The answer was {user_guess}")
       return True
   
def game():
    global turns
    print("Welcome to the Number Guessing Game!")
    
    answer = randint(1,100)

    set_difficulty()

    is_correct = False
    while not is_correct and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number")

        try:
            guess = int(input("Make a guess:"))
        except:
            print("Guess again")
            continue

        is_correct = check_answer(guess,answer)
        if not is_correct:
            turns -= 1
            if turns == 0:
                print("You've run out of guesses. Refresh the page to run again.")
            else:
                print("Guess again")

game()