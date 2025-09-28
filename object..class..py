class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def yep(self):
        print(f"Hello , my name is {self.firstname} {self.lastname} , i'm glad to meet you")


TheGuy=Person('Sarkodie','Frimpong')
TheGuy.yep()

