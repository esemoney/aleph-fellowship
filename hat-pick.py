import random

# first I create a list, hat to hold the cards.
hat = []

# function to create the card
def make_card(k):

    if k <= 7:

        card = 2 ** (k - 1)

        hat.append(card)

        return f"{card} was added to the hat!"
    return "K must be between 1 and 7!"

for x in range(1, 8):
    print(make_card(x))

total = 0

# keep picking randomly from the hat till the sum exceeds 124
while total < 124:
    pick = random.choice(hat)
    print(f"\nThe pick was {pick}")

    total += pick

    print(f"The sum is {total}")

    hat.remove(pick)


print(f"The most probable sum is {total}.")
