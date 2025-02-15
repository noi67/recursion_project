import random

min = int(input('Tell me a minimum number?\n'))
max = int(input('Tell me a maximum number?\n'))

if min > max:
    print("error: max must be bigger than min")
    exit()

secret_number = random.randint(min, max)

while True:
    guess = int(input("Guess the number\n"))
    
    if guess == secret_number:
        print("right!")
        break
    else:
        print("wrong!")




