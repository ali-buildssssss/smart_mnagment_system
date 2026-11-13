
from abc import ABC,abstractmethod


class Person(ABC):
    
    @abstractmethod
    
    def show_role(self):
        pass
    
    def __init__(self,name,age,person_id):
        self.name=name
        self.age=age
        self.person_id=person_id
        
    def show_info(self):
        print(f" The name is {self.name}\n The age is {self.age}\n The person_id is: {self.person_id}")

class address:
    def __init__(self,city,country):
        self.city=city
        self.country=country
    def show_address(self):
        print(f" Country: {self.country}\n city: {self.city}")
class course:
    def __init__(self,course,credits):
        self.course=course
        self.credits=credits
    def show_course(self):
        print(f" Courses \n course: {self.course} \n credits: {self.credits}")  
    
class Student(Person):
    def __init__(self, name, age, person_id,department,semester,city,country,credits,course_name):
        super().__init__(name, age, person_id)
        self.department=department
        self.semester=semester
        
        self.address=address(city,country)
        self.course=course(course_name,credits)
        
        self.__marks =[]
        

    def get_marks(self):
        return self.__marks
    
    
    def set_marks(self, *marks):
        for mark in marks:
            if 0<=mark<=100:
                self.__marks.append(mark)
    def show_marks(self):
        if self.__marks:
            print(f" The marks is {self.__marks}")
        else:
            print("invalid marks")
            
    def show_role(self):
        print(" I am a Student")
            
    def show_student_info(self):
        self.show_info()
        self.show_marks()
        self.address.show_address()
        self.course.show_course()
        print(f" Department: {self.department}\n Semester: {self.semester}")
        
class Teacher(Person):
    def __init__(self, name, age, person_id,subject,salary):
        super().__init__(name, age, person_id)
        
        self.subject=subject
        self.salary=salary
        
    def show_role(self):
        print(" I am a Teacher")
        
    def show_teacher_info(self):
        self.show_info()
        
        print(f" Subject: {self.subject}\n Salary: {self.salary}")
        
student=Student("ali",22,101,"cs",1,"MULTAN","PAKISTAN",3,"OOP")
teacher=Teacher("usama",25,202,"physics",25000)


while True:
    
    print("enter r for role of the person")
    print("enter m for enter  marks")
    print("enter s for seeing the information of of students")
    print("enter t for seeing the information of teachers")
    print("enter q for quiting")
    
    choice=input("enter your choices: ")
    if choice=="r":
        role=[student,teacher]

        for roless in role:
            roless.show_role()
    elif choice=="m":
        try:
            marks=int(input("enter marks: "))
        except ValueError:
            print("invalid,float and text not allowed")
        student.set_marks(marks)
        
    elif choice=="s":
           student.show_student_info()
    elif choice=="t":
          teacher.show_teacher_info()
          
    elif choice=="q":
        print("quiting...")
        break
    else:
        print("invalid choice! ")


