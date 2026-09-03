"""Higher or Lower: guess who has more Instagram followers.

Compare A vs B. If you are right, B becomes the new A and the score
goes up. Wrong guess ends the game.
"""

import random

data = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 610,
        "description": "Footballer",
        "country": "Portugal",
    },
    {
        "name": "Ariana Grande",
        "follower_count": 380,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 395,
        "description": "Actor and professional wrestler",
        "country": "United States",
    },
    {
        "name": "Selena Gomez",
        "follower_count": 428,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Lionel Messi",
        "follower_count": 490,
        "description": "Footballer",
        "country": "Argentina",
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 400,
        "description": "Reality TV personality and businesswoman",
        "country": "United States",
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 360,
        "description": "Reality TV personality and businesswoman",
        "country": "United States",
    },
    {
        "name": "Beyoncé",
        "follower_count": 315,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "Taylor Swift",
        "follower_count": 270,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "Neymar",
        "follower_count": 220,
        "description": "Footballer",
        "country": "Brazil",
    },
    {
        "name": "Kendall Jenner",
        "follower_count": 250,
        "description": "Model",
        "country": "United States",
    },
    {
        "name": "Justin Bieber",
        "follower_count": 280,
        "description": "Musician",
        "country": "Canada",
    },
    {
        "name": "Virat Kohli",
        "follower_count": 270,
        "description": "Cricketer",
        "country": "India",
    },
    {
        "name": "Nicki Minaj",
        "follower_count": 220,
        "description": "Musician",
        "country": "Trinidad and Tobago",
    },
    {
        "name": "Khloé Kardashian",
        "follower_count": 220,
        "description": "Reality TV personality",
        "country": "United States",
    },
    {
        "name": "Shakira",
        "follower_count": 150,
        "description": "Musician",
        "country": "Colombia",
    },
    {
        "name": "Drake",
        "follower_count": 140,
        "description": "Musician",
        "country": "Canada",
    },
    {
        "name": "Zendaya",
        "follower_count": 180,
        "description": "Actress and musician",
        "country": "United States",
    },
    {
        "name": "Kourtney Kardashian",
        "follower_count": 190,
        "description": "Reality TV personality",
        "country": "United States",
    },
    {
        "name": "Miley Cyrus",
        "follower_count": 200,
        "description": "Musician and actress",
        "country": "United States",
    },
]


def compare(a, b):
    """Return the celebrity dict with the higher follower_count."""
    if a["follower_count"] > b["follower_count"]:
        return a
    else:
        return b


score = 0
user = True
a = random.choice(data)

while user:
    b = random.choice(data)
    # Keep drawing B until it is a different person than A.
    while a == b:
        b = random.choice(data)

    print(f"Compare A: {a['name']} ({a['description']} from {a['country']})")
    print("vs")
    print(f"Against B: {b['name']} ({b['description']} from {b['country']})")

    choose = input("Choose between a and b: ").lower()
    winner = compare(a, b)
    if (choose == "a" and winner == a) or (choose == "b" and winner == b):
        print(f"You win!!! Current score {score}")
        score += 1
        a = b  # winner stays; next round they become option A
    else:
        print("You lose")
        user = False
