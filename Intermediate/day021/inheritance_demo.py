#inheritance demo

#this is the main class called animal
class Animal:
    def __init__(self):
        self.num_eyes=2
        
    def breathe(self):
        print("Inhale. Exhale")
        
#here fish class is not inheriting from fish class
class Fish:
    
    def swim(self):
        print("Moving in water")
        

nemo=Fish()
nemo.swim()

#with inheritance
class Fish(Animal):
    
    def __init__(self):
        super().__init__()
        
    #modifying breathe method 
    def breathe(self):
        super().breathe()
        print("doing this underwater")
    
    def swim(self):
        print("Moving in water")
        

nemo=Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)