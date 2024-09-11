
class Student:
    def __int__(self,name,rollno):
        self.name=name
        self._rollno=rollno
    def display(self):
        print(f"Hi myself {self.name} with rollno {self._rollno} from Student class")
class Branch(Student):
    pass

def showData():
 b1=Branch("Nisha",22)
 print(b1.name)
 print(b1._rollno)

showData()
# s1=Student("Rahul")
# print(s1.name)
# s1.display()
