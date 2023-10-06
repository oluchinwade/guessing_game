import random
def game():
    numb = random.randint(1,10)
    
    tries = 0
    max_tries =3
    while tries < max_tries:
        user = input("Guess the number:   ")
        user = int(user)
        tries +=1
        if user == numb:
            print('You guessed the right number, good job!')
            break
        elif user != numb:
            print(f'You still have {max_tries - tries} chances left')
            if user > numb:
                print('Hint, the number is less than this')
            elif user < numb:
                print('Hint, the number is more than this')            
        if tries == 3:
            print(f'Oh no you almost got it, the correct number was {numb}.')
            continue
            
    
            


game()

        
