print("========STUDENTS PERFORMANCE ANANLYSIS=======")
students={
    "101":{'name':'Aman','marks':[75,88,35]},
    "102":{'name':'Riya','marks':[9,32,45]}

}

def caltotal(marks):
    return sum(marks)
marks=students['101']['marks']

def avg(marks):
    return caltotal(marks)/len(marks)

def grad(average):
    if average>=75:
        return "Distinction"
    elif average>=60:
        return "First Division"
    elif average>=40:
        return "Pass"
    else:
        return "Fail"

def report(student):
    total=caltotal(student['marks'])
    average=avg(student['marks'])
    grade=grad(average)
    return{'total':total,'average':average,'grade':grade}
def main ():
    for i in students:
        s=students[i]
        r=report(s)
        print(i,"|",s['name'],"| Marks",s['marks'])
        print("total:",r['total'],"|Average:",r['average'],"|Grade:",r['grade'])
        print()
main()
def topstulist():
    
    return list(
        filter(
            lambda s:avg(s["marks"])>=75,
            students.values()
        )

    )
topstu=topstulist()
print("High performance")
for student in topstu:
    print(student["name"])
names = list(
    map(
        lambda s: s["name"],
        students.values()
    )
)

print("All Students :", names)
def flexible_average(*args):
    return sum(args) / len(args)
print("Flexible Average =", flexible_average(10,20,30,40))
def class_summary(**kwargs):

    print("\nClass Summary")

    for key, value in kwargs.items():
        print(key, ":", value)
class_summary(
    title="Student Report",
    passing_mark=40
)
def recursive_sum(n):

    if n == 1:
        return 1

    return n + recursive_sum(n - 1)

print("Recursive Sum =", recursive_sum(5))