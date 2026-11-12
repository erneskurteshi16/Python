age=18

if age==18:
    print("Equals 18")
elif age>=18:
    print("Over or equals 18")
else:
    print("Minor")

color='red'
in_city=True
if color!='green' and in_city:
    print("Don't move")
if color!='green' or in_city is False or 3>5 or 1!=1:
    print("You are free to drive")

#and, or, not in, in

studenti='Rigon'
students=['Rini','Edlira','Ernesi','Drini','Syari','Olti']

if studenti not in students:
    students.append(studenti)
else:
    print(students)

