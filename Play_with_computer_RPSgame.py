import random
import os
def clr():
    os.system("cls")
def res():
    return random.randint(0,2)
def game(m,b,x):
    a=res()
    if a==b:
        if x==1:
            print("Tie")
        else:
            return 't'
    elif a==0 and b==1:
        print("Round ",m,":Computer is rock You is paper You won")
        return 'b'
    elif a==1 and b==0:
        print("Round ",m,":Computer is paper You is rock Computer won")
        return 'a'
    elif a==1 and b==2:
        print("Round ",m,":Computer is paper You is scissors You won")
        return 'b'
    elif a==2 and b==1:
        print("Round ",m,":Computer is scissors You is paper Computer won")
        return 'a'
    elif a==2 and b==0:
        print("Round ",m,":Computer is scissors You is rock You won")
        return 'b'
    elif a==0 and b==2:
        print("Round ",m,":Computer is rock You is scissors Computer won")
        return 'a'
n=int(input("Enter how many rounds"))
clr()
awin=0
bwin=0
m=0
x=int(input("Do you want to consider tie?\nIf yes enter 1 \nIf not enter 0\n"))
clr()
print("PRESS\n0.rock\n1.paper\n2.scissors")
print("NOW START\n")
if x==0:
    for i in range(n):
        m=m+1
        b=int(input("enter your choice"))
        result = game(m,b,x)
        if result=='a':
            awin=awin+1
        elif result=='b':
            bwin=bwin+1
        while result =='t':
            result=game(m,b,x)
            if result=='a':
                awin=awin+1
            elif result=='b':
                bwin=bwin+1
    print("Computer won:",awin,"You won:",bwin)
elif x==1:
    for i in range(n):
        m=m+1
        b=int(input("enter your choice"))
        result = game(m,b,x)
        if result=='a':
            awin=awin+1
        elif result=='b':
            bwin=bwin+1
    print("Computer won:",awin,"You won:",bwin)