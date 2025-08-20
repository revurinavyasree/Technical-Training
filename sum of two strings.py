a="123"
b="342"
num1=0
for i in a:
    x=ord(i)-ord("0")
    num1=(num1*10)+x
num2=0
for i in b:
    x=ord(i)-ord("0")
    num2=(num2*10)+x
print(num1+num2)
