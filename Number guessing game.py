 secret = 27
attempts = 0
max_attempts = 5
guessed = False

while attempts < max_attempts :
guess = int(input("Guess the number (1-50): "))
attempts = attempts + 1

if guess == secret:
 print("You win!")
 break

