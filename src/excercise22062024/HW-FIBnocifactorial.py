"""
Task #10 -
✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24
"""
n = int(input("Entre the number to find factorial of: "))
res = 1
if n == 0:
    print(1)
else:
    for i in range(1, n + 1):
        res = res * i
    print(f"The factorial of {n} is {res}")

"""
Task #11 -
✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13
"""

f = int(input("Entre the number to find fibanocci of: "))
a = 0
b= 1
fib = 0
if f==0:
    print(0)
elif f==1:
    print(0)
else:
    for i in range(2,f+1):
        fib=a+b
        a=b
        b=fib
    print(fib)




