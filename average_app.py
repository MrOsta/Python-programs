try:


    
    class Student():
        
        def __init__(self, name):
            self.name = name
            self.marks = []
            print("Welcome {} To The Program, By:Me, twitter:@YaqubAlrubiaan.\n ---------".format(name))
        
        def add_marks(self, mark):
            self.marks.append(mark)
        def avg(self):
            return sum(self.marks)/len(self.marks)
    user = input("What's your name?: ")
    howmuch = int(input('How many articles ?(only numbers):'))
    x = Student(user)
    
    for i in range(howmuch):
        c = x.add_marks(int(input('How many marks are you in article {} (only numbers) ?:  '.format(i+1))))
    
    print("\n ------------ \n The Marks is:",x.marks)
    
    print("\n ------------ \n The Average is:",x.avg())
    
except:
    print("\n ################# \n There's An Error, Please Check the data \n ################# \n Or Contact Me:- \n Twitter: @YaqubAlrubiaan")