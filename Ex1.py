""" 
Rafael Díaz Medina Science Computer student from Tecnologico de Monterrey

Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
 You should use input to read a string and float() to convert the string to a number. 
 Do not worry about error checking or bad user data. """


n = input("N: ")
if int(n)>0:
    print("n es positivo")
    if int(n)<5:
        print("n es menor a 5 pero es positivo")
    else:
        print("n es un buen numero")
    print("Sali del segundo if")
else:
    print("n es negativo")

print("Salida")
