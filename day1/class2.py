#list
lst_1 =[1,2,3,4]
lst_1=[2,"ram", 3.4]
print(lst_1)

item_1 = 'value 1'
item_2 = 66
item_3 = 'value 3'

lst_2 = [item_1, item_2, item_3]
lst_3 =['item_1', 'item_2', 'item_3']

print(lst_2, lst_3)

student=['name', 4, '3.7', 'D']
print(student[0])
print(student[3])
print(student[1])
print(student[2])

print(len(student)) #student to length find garne


#dictionary 

name=str(input("enter name:"))
roll= int(input("enter roll number:"))
gpa=float(input("enter gpa:"))
section=str(input(" enter section:"))

student={
    'name': name,
    'roll': roll,
    'gpa': gpa,
    'section':section,
}




print(student['gpa'])
student['college']='texas'
print(student)

