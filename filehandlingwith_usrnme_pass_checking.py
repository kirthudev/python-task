def textodic():

  d={}
  f=open(r"E:guvigeeks.txt","r")
  for line in f:
    (key,val)=line.strip().split()
    d[key]=val
  print(d)

  if a in d:
    if b==d[a]:
        print("valid")
    else:
        print("incorrect")
  else:
    print("invalid")
def passchr():
    if (b2 > 15 and b2 < 6):
        print("password must contain 6-15 characters")


import re
def splchr():
    
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (regex.search(b) == None):


        print("password should have one special characters")

def uppr():
    count=0
    for i in range(b2):
        if(b>="A" and  b<="Z"):
            count=count+1
            if(count>0):
                break
        else:
            print("password must contain atleast one uppercase")
            break
a,b=input().split("=")
a2=len(a)
b2=len(b)
passchr()
splchr()
uppr()
if ('@' and "." not in a):
    print("enter a valid input,use '@' and '.' in the user name")
else:
    textodic()
