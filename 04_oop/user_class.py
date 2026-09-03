"""OOP basics: a User class with attributes and a follow method.

Class names use PascalCase. __init__ runs when you create an object
and sets its starting data (attributes).
"""


class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.follower = 0  # default attribute
        self.following = 0

    def follow(self, user):
        """This user follows another user: their followers go up, our following goes up."""
        user.follower += 1
        self.following += 1


# An attribute is a variable attached to an object (user_3.username).
user_3 = User("003", "rishab")
print(user_3.username)

# --- earlier way: set attributes one by one after creating the object ---
# user_1 = User()
# user_1.id = "001"
# user_1.username = "anurag"
# print(user_1.username)
