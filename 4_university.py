class admissions:
    def __init__(self):
        self.id=None
        self.age=None
        self.marks=None

    def validate_marks(self):
        if (self.marks>=0 and self.marks<=100):
            return True
        else:
            return False

    def validate_age(self):
        if self.age>=20:
            return True
        else:
            return False

    def check_qualification(self):
        if (self.validate_marks() and self.validate_age()):
            if self.marks>=65:
                return True
            else:
                return False
        else:
            return False

    def set(self):
        self.id=int(input("Enter id:"))
        self.age=int(input("Enter age:"))
        self.marks=int(input("Enter marks:"))
        print("\n")
            
    def get(self):
        print("Marks:{}".format(self.validate_marks()))
        print("Age:{}".format(self.validate_age()))
        if self.check_qualification():
            print("Admission accepted.")
        else:
            print("Admission denied.")
        print("\n")
        
                
n = int(input("Enter the number of students:"))
l=[]
for i in range(n):
    i = admissions()
    l.append(i)
    i.set()
for i in l:
    i.get()

            

    
