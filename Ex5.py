"""
Rafael Díaz Medina Science Computer student from Tecnologico de Monterrey
Worked exercise 5.1

"""
num=0.0
total=0.0
count=0
while True:
    numIn=input("give me a number: ")
    if numIn=="Done":
        break
    try:
        num=float(numIn)
    except:
        print("Invalid Input")
        continue
    total=num+total
    count+=1
print(total, count, total/count)
    