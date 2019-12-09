u1={"name":"kiki","accno":1234,"balance":5000,"pass":"2837"}
def withdraw():
  w1=int(input("enter the amount you want to withdraw"))
  if w1>u1["balance"]:
      print("you dont have sufficient balance")
  else:
     a=u1["balance"]
     b=a-w1
     u1.update(balance=b)
  print("balance is :",u1["balance"])
def deposit():
  d1=int(input("enter the amount you want to deposit"))
  c=u1["balance"]
  d=c+d1
  u1.update(balance=d)
  print("your current balance is",u1["balance"])
def balance_enquiry():
    print("name:",u1["name"])
    print("account number is",u1["accno"])
    print(u1["balance"],"is the current balance")
def cal():
   c=input("select transactions:1->deposit  2->withdrawl 3->balance enquiry")
   if c=="1":
      deposit()
      d=input("dp you want to continue press yes")
      if d=="yes":
          cal()
      else:
          print("thnk you")
   elif c=="2":
      withdraw()
      d = input("dp you want to continue press yes")
      if d == "yes":
          cal()
      else:
          print("thnk you")
   elif c=="3":
       balance_enquiry()
       d = input("dp you want to continue press yes")
       if d == "yes":
           cal()
       else:
           print("thnk you")
   else:
      print("no tansactions selected.....thank you")
cal()
