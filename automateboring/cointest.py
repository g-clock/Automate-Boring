import random
guess = " "
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
for i in range(0, 1):
    if toss == 0:
        print('You got it!\n')
    else:
        print('Nope! Guess again!')
guess = input()

if toss == 0 and guess is not 1:
    print('You got it!\n')
else:
    print('Nope! Guess again!')
elif toss == 1 and guess is not 0:
    print('You got it!\n')
else
    print('Nope. You are really bad at this game.')
    guess = input()
if toss == 1 and guess is not 0:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
