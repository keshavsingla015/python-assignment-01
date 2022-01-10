details_required = ['name','sid','cgpa','gender','course_name']

name=(input("what is your name: "))
sid=(int(input('put down your sid: ')))
cgpa=(float(input('tell your CGPA:')))
gender=(input('Gender: (M/F/U) '))
course_name=(input("Under which course: "))
print(details_required)

details = [name,sid,cgpa,gender,course_name]
print(details)