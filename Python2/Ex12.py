"""
Rafael Díaz Medina Science Computer student from Tecnologico de Monterrey

9.4 Write a program to read through the mbox-short.txt and figure out who has sent 
the greatest number of mail messages. The program looks for 'From ' lines and takes 
the second word of those lines as the person who sent the mail. The program creates 
a Python dictionary that maps the sender's mail address to a count of the number of 
times they appear in the file. After the dictionary is produced, the program reads through 
the dictionary using a maximum loop to find the most prolific committer.
Output
cwen@iupui.edu 5
"""

fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fname)
bigWord=None
bigCount=None
mails= dict()

for line in handle:
    if not line.startswith("From ") : 
        continue
    parts=line.split()
    mail=parts[1]
    mails[mail]=mails.get(mail, 0)+1

for key,count in mails.items():
    if bigCount is None or count> bigCount:
        bigCount=count
        bigWord= key
print(bigWord, bigCount)


