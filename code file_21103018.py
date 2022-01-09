#QUESTION1
a = int(input('enter first number: '))
b = int(input('enter second number: '))
c = int(input('enter third number: '))

average = str(a + b + c / 3)

print(average)

#QUESTION2
income = int(input('enter your income:$ '))
dependents = int(input("number of dependents on you: "))

income_tax = (income*0.20) - 10000 - (dependents*3000)

payable_tax = str(max(0,income_tax))

print('your payable tax is $' + payable_tax)


#QUESTION3
details_required = ['name','sid','cgpa','gender','course_name']

name=(input("what is your name: "))
sid=(int(input('put down your sid: ')))
cgpa=(float(input('tell your CGPA:')))
gender=(input('Gender: (M/F/U) '))
course_name=(input("Under which course: "))
print(details_required)

details = [name,sid,cgpa,gender,course_name]
print(details)


#QUESTION4
marks_1= int(input('enter marks of first student: '))
marks_2= int(input('enter marks of second student: '))
marks_3= int(input('enter marks of third student: '))
marks_4= int(input('enter marks of 4th student: '))
marks_5= int(input('enter marks of 5th student: '))

list = [marks_4,marks_5,marks_3,marks_2,marks_1]

print(list)
print()
print('Marks in Ascending Order')
list.sort()
print(list)
print()
print("Marks in Decreasing order")
list.reverse()
print(list)



#QUESTION5
# PART A
print('A.')
list = ['Red','Green','White','Black','Pink','Yellow']
print(list)  #input given
list.remove('Black')
print(list)  #output

#PART B
print( )
print('PART B')
list2 = ['Red','Green','White','Black','Pink','Yellow']
print(list2)
list2[3]='Purple'  #replacing black with purple using n-1 term operation
list2[4]='Purple'

print(list2)
