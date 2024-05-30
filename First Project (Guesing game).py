import random

print ('''

***** This is a guessing game *****
       
- You first need to choose a number, then the computer will pick a randon number between 0 and the number you choose

- If you guess the number from the first time you are very lucky

- at the end we will give you the number of guessess you tried until you got the number

***** Thank you for playing *****
''')

a = input('Type a number: ')

if a.isdigit():
    a =int(a)
    if a <= 0:
         print ('Please type a number larger than 0 next time. ')
         quit()
else:
        print('Please type a number next time')
        quit()

rn = random.randrange(a)
guesses = 0

while True:
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
     user_guess  = int(user_guess)
    else:
        print ('Please type a number next time.')
        continue
    guesses +=1
    if user_guess == rn:
        print ('You got it')
        break
    
    if user_guess > rn:
        print('You were above the number!')
        if guesses >= 5 and  user_guess > rn:
         print('try this number', user_guess - (user_guess - rn))
    elif user_guess < rn:
        print('You were below the number!')
        if guesses >= 5 and  user_guess < rn:
            print('try this', user_guess + (rn - user_guess)) 

        

        
        
print ('You got it in' ,guesses, 'guesses')