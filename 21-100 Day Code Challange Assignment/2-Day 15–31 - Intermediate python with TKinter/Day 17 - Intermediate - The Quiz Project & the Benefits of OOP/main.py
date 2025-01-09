# Creating a Class or Class Declaration
class User:
    def __init__(self, user_id, username):
        # Adding Attributes to a Class
        self.id = user_id
        self.username = username
        self.followers = 0  # Attribute's Default Value
        self.following = 0  # Attribute's Default Value

    # Adding Method to a Class
    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Daffa"

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Ucup"

# Dibandingkan cara diatas, cara dibawah ini lebih best practice
user_1 = User("001", "Daffa")
user_2 = User("001", "Ucup")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
