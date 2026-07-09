class Instagram:
    def __init__(self,username,name):
        self.username=username
        self.name=name
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1
        

user1=Instagram("mv1","max")
print(user1.followers) #prints 0 as the followers of any object created from the class is set to 0 by default

user2=Instagram("rs45","rohit")
user1.follow(user2)

print(user1.following)
print(user2.followers)

