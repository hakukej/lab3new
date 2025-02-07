def toounces(grams):
    a = 28.3495231*grams
    print(f"{grams} grams in ounces is {a}")

toounces(5)

def centigrade(f):
    a = (5/9)*(f-32)
    print(f"for {f} the centigrade is {a}")

centigrade(50)

def solve(numheads, numlegs):
    for chickens in range(numheads):
        rubbits = numheads - chickens
        if(2*chickens + 4*rubbits == numlegs):
            print(f"{chickens} chickens and {rubbits} rubbits")
solve(35, 94)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:  
            return False
    return True 
def filterprime(numbers):
    return list(filter(is_prime, numbers))
numbers = list(map(int, input().split()))

prime_numbers = filterprime(numbers)

print("Простые числа:", prime_numbers)

from itertools import permutations

def print_permutations(s):
    perms = permutations(s) 
    for p in perms:
        print("".join(p))

word = input("the word:")
print_permutations(word)

def reverse_words(sentence):
    words = sentence.split() 
    reversed_sentence = " ".join(reversed(words))  
    return reversed_sentence

sentence = input("sentence: ")
print(reverse_words(sentence))

def three(a):
    arr=[]
    for i in range(a):
        elem = int(input())
        arr.append(elem)
    for i in range(len(arr) - 1):
        if arr[i] == 3 and arr[i+1] == 3:
            return True
    return False
a = int(input())
if three(a):
    print("True")
else:
    print("False")