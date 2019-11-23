import random
import time

# generate a pack of cards in memory
# we don't need to see the cards until we play the game
# each card is a unique key 1..52 and value e.g. (twoC, 2)
cards=["ace","two","three","four","five","six",\
       "seven","eight","nine","ten","j","q","k"]
suites = ["C", "D", "H", "S"]

deck = {}
count = 0
for card in cards:
    for suite in suites:
        deck[str(count)] = (card+suite, int(1+count/4))
        count += 1

# now play the game
# start with 2 cards chosen at random from the pack
score = 0
time.sleep(2)
print("here are your cards")
for x in range(2):
    twist = random.randint(1, 52)
    card_file = open(deck[str(twist)][0])
    print(card_file.read(1000))
    score += deck[str(twist)][1]

# check for pontoon and the player's stick or twist
print("you got {}".format(score))
if score == 21:
    print("Pontoon - you win!")
else:
    choice = input("do you want to twist? y/n:   ")

# twist one card and check the score
while choice == "y":
    twist = random.randint(1, 52)
    card_file = open(deck[str(twist)][0])
    print(card_file.read(1000))
    score += deck[str(twist)][1]

    # did the player finish?
    print("you got {} ".format(score))
    choice = "n"
    if score < 21:
        choice = input("do you want to twist? y/n:  ")
    if score == 21:
        print("pontoon!")
    if score > 21:
        print("you are busted!")

# game over