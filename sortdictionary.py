from operator import itemgetter
students = [
    {'Name': 'Ritika', 'Age': 19},
    {'Name': 'Sumaira', 'Age': 19},
    {'Name': 'Sania', 'Age': 20},
    {'Name': 'Ruchika', 'Age': 20},
    {'Name': 'Anshika', 'Age': 20},
    {'Name': 'Sanjh', 'Age': 19},
    {'Name': 'Gurman', 'Age': 18}
]
sorted_students = sorted(students, key=itemgetter('Name'))
print("Sorting the list of dictionaries by Name:")
for student in sorted_students:
    print(student)