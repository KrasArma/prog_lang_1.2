
a = float(input('первое число '))
b = float(input('второе число '))
c = str(input('что делаем? '))

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif (c == ":" or c == "/"):
    if b != 0:
        print(a/b)
    else:
        print('так не получится')
else:
    print('неверный символ')