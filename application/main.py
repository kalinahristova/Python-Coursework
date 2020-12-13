from Student import *

def heppy_student():
    stud.birthday()
    stud.print()

def student_finish_year():
    stud.finish_year()
    print("New fee for year "+str(stud.year)+" is: ", end="")
    print(f'{stud.fee:.2f}')

def student_print():
    stud.print()

def is_student_graduate():
    stud.graduate()

stud = None
st_name = ""
st_city = ""
st_street = ""
st_number = 0
st_age = 0
st_program = ""
st_fee = 0.00
while True:
    print("Select:")
    print("1. Create new Student")
    print("2. Show Student details")
    print("3. Happy Birthday")
    print("4. Finish Year")
    print("5. Can Student gratuate")
    print("0. Exit Program")
    ans = int(input("Enter your choice: "))
    if ans == 0:
        print("Program exit!")
        break
    if ans == 1:
        st_name = input("Enter Student names: ")
        st_city = input("Enter Student City: ")
        st_street = input("Enter Student Street: ")
        st_number = int(input("Enter Student Street Number: "))
        st_age = int(input("Enter Student Ages: "))
        st_program = input("Enter Sudent Program: ")
        st_fee = float(input("Enter Student Fee: "))
        stud = Student(st_name, st_city, st_street, st_number, st_age, st_program, 1, st_fee)
        continue
    if ans == 2:
        student_print()
        continue
    if ans == 3:
        heppy_student()
        continue
    if ans == 4:
        student_finish_year()
        continue
    if ans == 5:
        is_student_graduate()
