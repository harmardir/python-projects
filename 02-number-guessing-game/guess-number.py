import random

print("Hi what's your name ?")
name = input()

print("Nice to meet you " + name + " Let's play a game\n")
print("I will think of a number between 1 and 20 and you have to guess it in less than 6 guesses\n")

number = random.randint(1, 20)

guesses_no = 0

while (guesses_no < 6):
    print("Take a guess: \n")
    guess = input()
    guess = int(guess)
    guesses_no += 1
    if(guess < number):
        print("Wrong ! your guess is lower than the number\n")
    if(guess > number):
        print("Wrong ! your guess is higher than the number\n")
    if (guess == number):
        break
if(guess == number):
    print("Good job " + name + " ! you guessed my number in " + str(guesses_no) + " guesses !")
elif(guess != number):
    print("Sorry ! The number I was thinking of is: " + str(number))
    print("Try again next time !")

