# smart_mnagment_system
Student & Teacher Management (Python OOP)

A small command-line project I built to practice Object-Oriented Programming in Python. It models a student and a teacher, stores their details, and lets you interact with them through a simple text menu.

Nothing fancy, no database, no external libraries. Just clean OOP concepts put to work.

What it does

When you run the program, you get a menu where you can:

r: see the role of each person (Student / Teacher)
m: enter marks for the student
s: view the student's full information (personal info, marks, address, course, department, semester)
t: view the teacher's information (personal info, subject, salary)
q: quit
OOP concepts used

I wrote this mainly to understand how these ideas fit together:

Concept	Where it shows up
Abstraction	Person is an abstract class with an abstract show_role() method, so every kind of person must define its own role
Inheritance	Student and Teacher both inherit from Person and reuse name, age, person_id and show_info()
Encapsulation	A student's marks are stored in a private list (__marks) and only changed through set_marks() / read through get_marks()
Composition	A Student has an address and has a course, which are their own small classes
Polymorphism	show_role() is called on both a student and a teacher in one loop, and each responds in its own way
Project structure
Person (abstract)
├── Student   -> has an address, has a course, keeps private marks
└── Teacher   -> has a subject and a salary

address       -> city, country
course        -> course name, credits
How to run it

You only need Python 3 installed.

bash
git clone <your-repo-url>
cd <your-repo-folder>
python main.py

(Replace main.py with whatever you named the file.)

Example session
enter r for role of the person
enter m for enter  marks
enter s for seeing the information of of students
enter t for seeing the information of teachers
enter q for quiting
enter your choices: r
 I am a Student
 I am a Teacher
A few things to know
The student and teacher are created with sample data (Ali and Usama) at the bottom of the file. Change them to whatever you like.
Marks are only accepted if they are between 0 and 100. Anything outside that range is quietly ignored.
Marks must be whole numbers. Text and decimals show an error message.
Ideas for improving it
Let the user create students and teachers from the menu instead of hard-coding them
Support multiple students and teachers
Save data to a file or database
Calculate average marks and grades
Split the classes into separate files
About

Made as a learning project while studying OOP. Feedback and suggestions are always welcome!
