def histogram():
    a = int(input())
    arr=[]
    for i in range(a):
        elem = int(input())
        arr.append(elem)
    for i in range(len(arr)):
        print("*" * arr[i])


import random
def guess():
    print("Hello! What is your name?")
    name = str(input())
    print("Well, "+ name +", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    number = random.randint(1 , 20)
    a = int()
    count = 0
    while a!= number:
        count += 1
        a = int(input())
        if a < number:
            print("Your guess is too low")
            print("Take a guess.")
        elif a > number:
            print("Your guess is too great")
            print("Take a guess")
        else:
            print("Good job, " + name + "! You guessed my number in "+ str(count) +" guesses!")


def palin(s):
    s = s.lower()
    s.replace(" ","")
    if s == s[::-1]:
        return True
a = str(input())
if palin(a):
    print("YES")
else:
    print("NO") 

def unique():
    a = int(input())
    arr=[]
    answer=[]
    for i in range(a):
        elem = int(input())
        arr.append(elem)
    for i in arr:
        if i not in answer:
            answer.append(i)
    print(answer)


s = 'word'
if palin(s):
    print("YES")
else:
    print("NO")
unique()
guess()
histogram()