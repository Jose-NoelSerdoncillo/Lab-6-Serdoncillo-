age = int(input("Enter your age:"))
status = input("Do you have a membership status?")
if age>= 1 and age < 18:
    if status =="Yes":
        print("Your fee is 450.00 pesos")
    elif status == "No":
        print("Your fee is 650.00 pesos")     
elif age>=18 and age <=65:
    if status =="Yes":
        print("Your fee is 550.00 pesos")
    elif status == "No":
        print("Your fee is 750.00 pesos")
elif age > 65:
    if status =="Yes":
        print("Your fee is 550.00 pesos")
    elif status =="No":
        print("Your fee is 750.00 pesos")
else:
    print("invalid input")       