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