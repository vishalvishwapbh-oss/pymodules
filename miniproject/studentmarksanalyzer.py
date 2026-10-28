sbjects=('Python','Maths','DBMS')
print("sbjects : ",sbjects)
n=int(input("How many students?"))
students=[]
for i in range(n):
    print("Enter details of student",i+1)
    stuid=input("Student ID : ")
    name=input("Student Name : ")
    python=int(input("enter the py marks : "))
    maths=int(input("enter the maths marks : "))
    dbms=int(input("enter the dbms marks : "))
    marks={
        "python":python,
        "maths":maths,
        "dbms":dbms
    }
    totalmarks=python+maths+dbms
    avg=totalmarks/3
    if avg>=75:
        result="excellance"
    elif avg>=40:
        result="pass"
    else:
        result='fail'
    student={
            "id":stuid,
            "name":name,
            "marks":marks,
            "totalmarks":totalmarks,
            "avg":avg,
            "result":result
        }
    students.append(student)
print("==========Student Reports=========")
for student in students:
    print(student["id"],"|",student["name"])
    print("python : ",student["marks"]["python"],",maths : ",student["marks"]["maths"],"dbms : ",student["marks"]["dbms"])
    print("total : ",student["totalmarks"])
    print("avg : ",student["avg"])
    print("Result : ",student["result"])
    print()
