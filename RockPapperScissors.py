import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Gains, %s Pertes, %s Egalités' % (wins, losses, ties))
    while True: # The player input loop.
        print('Quel est ton choix:  (P)ierre (p)apier (c)iseaux ou (q)uiter ?')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'P' or playerMove == 'p' or playerMove == 'c':
            break # Break out of the player input loop.
        print('Ecris soit P, p, c, ou q.')

    if playerMove == 'P':
        print('Pierre VS...')
    elif playerMove == 'p':
        print('Papier VS...')
    elif playerMove == 'c':
        print('Ciseaux VS...')


    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'P'
        print('Pierre')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Papier')
    elif randomNumber == 3:
        computerMove = 'c'
        print('Ciseaux')

    if playerMove == computerMove:
        print('Egalité!')
        ties = ties + 1
    elif playerMove == 'P' and computerMove == 'c':
        print('Gagné')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'P':
        print('Gagné')
        wins = wins + 1
    elif playerMove == 'c' and computerMove == 'p':
        print('Gagné')
        wins = wins + 1
    elif playerMove == 'P' and computerMove == 'p':
        print('Perdu')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'c':
        print('Perdu')
        losses = losses + 1
    elif playerMove == 'c' and computerMove == 'P':
        print('Perdu')
        losses = losses + 1