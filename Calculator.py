# Simple Calculator
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multiple(a, b):
    return a*b
def devision(a, b):
    return a//b
print(""""
Select Your Choise:
1.Add
2.Sub
3.Multiple
4.Devition
""")
choise =int(input("Enter Your Choise:"))
if choise == 1 or choise==2 or choise==3 or choise==4:
    First_Value =int(input("First Value:"))
    Second_Value =int(input("Second Value:"))
    if choise == 1:
        print("Answer is ", add(First_Value, Second_Value))
    elif choise == 2:
        print("Answer is ", sub(First_Value, Second_Value))
    elif choise == 3:
        print("Answer is ", multiple(First_Value, Second_Value))
    elif choise ==4:
        print("Answer is ", devision(First_Value, Second_Value))
    else:
        print("***Invalid Input***")
else:
    print("Please Choose the Valid Option")