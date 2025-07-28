import random
user_input = input("Guess a number between 1 and 100: ")
num_to_guess = random.randint(1,100)
while True:
   try:
     guess = int(input('guess number between 1 to 100: '))

     if guess < num_to_guess:
        print('Too low')
     elif guess > num_to_guess:
        print('Too high')
     else:
        print('Congratulations! You guessed the number!')
        break
   except ValueError:
    print('Enter a valid number')

