def category():
    print("choose vehicle category")
    print("Bike- price 8rs/km")
    print("Car- price 30rs/km")
    print("Auto- price 15rs/km")
    cat = input()

    if cat=="Bike":
        price=kilometers*8
    elif cat=="car":
        price=kilometers*30
    else:
        price =kilometers *15

    print(price,"total price of your journey")

    print(name,DoB,mailid)





name=input("enter your Name:")
DoB=input("enter your date of birth:")
mailid=input("enter your mail id:")
print("************************************************")
so=input("enter the source location")
de=input("enter your destination")
if "-" in so and de:
       print("invalid")

elif so.isalpha() and de.isalpha():
        print("enter proper input location")
        pass

else:
    s1 = float(so)
    s2 = float(de)
    kilometers = s2 - s1
    print(kilometers, "total kms")
    category()
