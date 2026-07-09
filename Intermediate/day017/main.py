# Understanding the need of using classes and objects ->

class User:
    pass

user1=User()
user1.id="007"
user1.username="Bond"

print(user1.username)

user2=User()
user2.id="009"
user2.username="max"

print(user2.id)


# Using objects and classes with constructor -> 

class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username

user1=User("001","verstappen")
print(user1.id)
print(user1.username)