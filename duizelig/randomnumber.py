from random import randint 
guesses = 1 
number = randint (1,10) 
rounds = 1 
maximumrounds = 20
print (number) 
guess = int(input("guess a number between 1 and 10"))

while guess != number: 
    if guess < number:
        print ("your guess was too low") 
        guess = int(input("please guess again: "))
        guesses = guesses + 1 
        rounds = rounds + 1
    elif guess > number: 
        print ("your guess was too high") 
        guess = int(input("please guess again: "))
        guesses = guesses + 1
        rounds = rounds + 1
    if guesses == 10: 
        print ("youve reached the maximum amount of tries") 
    if maximumrounds == 2:
        print ("youve reached the maximum amount of tries") 
        break 
    maximumrounds = rounds 


if guess == number:
    rounds = rounds + 1 
    maximumrounds = rounds 
    print ("youve guesses the number") 
    from random import randint
    number = randint (1,10) 
    guess =int(input("please guess again"))
if maximumrounds == 3:
     ("youve done the maximum amount of tries") 



    
  
    

        
        


     



