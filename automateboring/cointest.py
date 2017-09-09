import random
guess = " "
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
for i in range(0, 1):
    if toss == 0 and not 1:
        print('You got it!\n')
    if toss == 1 and not 0:
        print('You got it!!\n')
    else:
        print('Nope. Try again.')

        guess = input()
    if guess is ('heads', 'tails'):
        print('You were correct')

else:
    print('Game over')
