def greet(emri):
    print(f"Hello {emri}!")

student1='Drini'
students=['Drini','Edlira','Ernesi','Olti','Syari']

for student in students:
    greet(student)

print("----------"*3)

def power(nr:int, pow:int)->int:
    return nr**pow

#power(nr=5,pow=3)
result =power(pow=3,nr=5) #implicite
print(result)

def rectangle_area(a:float,b:float)->float:
    area = a*b #kjo variabel nuk ka scope jashte funksionit
    return round(area,2)

print("Siperfaqja e drejtkendshit eshte: ",rectangle_area(10.0,4.5),"njesi katrore")

def circle_area(radius=5.5): #vlera by default e parametrit merret vetem ne rastet kur nuk i dergojm argument
    global pi #global ka scope jashte funksionit
    pi=3.14
    return pi*(radius**2)

rrethi1=circle_area(10.33)
print("Vlera e konstantes pi eshte: ",pi)
print(rrethi1)
