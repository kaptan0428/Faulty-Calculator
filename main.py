#  Faulty calculator
# 45*3=100; 23+6=40; 45/5= 5 : These are faults
a = int(input("Enter first no. : "))
b = int(input("Enter second no. : "))
oper = input("Enter operator :")
if a==45 and b==3 and oper=='*':
    print("100")
elif a==23 and b==6 and oper=='+':
    print("40")
elif a==45 and b==5 and oper=='/':
    print("5")
elif oper=='*':
    print(a*b)
elif oper=='+':
    print(a+b)
elif oper=='/':
    print(a/b)
else:
    print("Error! unexpected input")
