"""
Rafael Díaz Medina Science Computer student from Tecnologico de Monterrey

In this assignment you will read through and parse a file with text and numbers.
 You will extract all the numbers in the file and compute the sum of the numbers.


"""
import re
name = "regex_sum_952250.txt"
handle = open(name)
final=0

for line in handle:
    rex=re.findall('[0-9]+', line)
    if len(rex)==0:
        continue
    for n in rex:
        b=int(n)
        final+=b
print(final)