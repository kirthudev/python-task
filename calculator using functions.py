def add(a,b):
     c=a+b
     print(c)
def sub(a,b):
     c=a-b
     if(a<b):
        print("answer will get negative value")
     print(c)
def mul(a,b):
     c=a*b
     #if(a==0 or b==0):
       # print("logical error")
    
     print(c)
def div(a,b):
     
     if(b==0):
       print("divide by 0 error")
     else:
       c=a/b
     print(c)
def mod(a,b):
     c=a%b
     #if(b==0 or a==0):
       #print("logical error")
     print(c)
def again():
     calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO
''')

     if calc_again.upper() == 'Y':
        cal()
     elif calc_again.upper() == 'N':
        print('See you later.')
     else:
        again()

def cal():
  a=input("enter a value 1:")
  b=input("enter a value 2:")
  if "." in a or b:
       a=float(a)
       b=float(b)

  else:
       a=int(a)
       b=int(b)
       
  print(type(a))
  print(type(b))
  print("1 Addition")
  print("2 Subraction")
  print("3 Multiplication")
  print("4 Division")
  print("5 modulus")
  d=int(input("user choices 1 2 3 4 5->"))
   
  
  if d>5:
    print("the choice is not existed")
  elif(d==1):
    add(a,b)
  elif(d==2):
    sub(a,b)
  elif(d==3):
    mul(a,b)
  elif(d==4):
    div(a,b)
  elif(d==5):
    mod(a,b)
cal()
again()

