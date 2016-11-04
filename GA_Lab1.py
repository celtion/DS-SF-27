nums = range(10)
print nums

nums.append(10)
print nums

nums + [10]
print nums

stuff = {'name': 'Alan', 'age': 21, 'height': 6 * 12 + 2}
print stuff ['name']

d = {'a':10, 'b':20, 'c':30}
print d['a']
print d['b']
print d['c']
print d

d = {'a':10, 'b':20, 'c':30}
d['c'] = 40
print d

people = {'Alice': ['Washington', 'DC'], 'Brandon' :['Arlington', 'VA']}
print people['Brandon']

cal = 'a', 'b'
def cal():
    for letter in cal:
        total += letter
    return total

#number = int(raw_input("Enter a number to see if it is prime: "))
#if number <= 1:
#    print ("numbe it is not prime.")
#else:
#    a = 2
#    check = True
#    while a != number:
#        if number %a == 0:
    #        print ("Number is not prime.")
    #        check = False
    #        break
    #    a += 1
    #    if check == True:
    #        print ("Number is prime.")

#def printinfo (name, age):
    #print 'Name:', name
    #print 'Age:', age
    #return
#printinfo (age=44, name='Kul')

#youtube Trevor Payne basics#7 of 8 - Files and User
#def myFunc():
    #'''
#    I documented something.
    #'''
    #only seen in code view, comp ignores
    #pass
    #print myFunc.__doc__

#youtube Trevor Payne basics#7 of 8 - Files and User
#highest = 10
#answer = 7
#guess = raw_input("guess a number from 0 to %d: " %highest) #basically it means from 0 -10
#while (int(guess)!= answer):
#    if(int(guess)< answer):
    #    print "answer is higher"
#    else:
    #    print "answer is lower"
    #guess = raw_input("guess a number from 0 to %d: " %highest)
#raw_input("you are a winner face!")

#The prime factors of 13195 are 5,7,13 and 29.
#What's the largest prime factor of 600851475143?

    #code not working

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
print (n)

def largest_prime_factor(n):
    primfact = []
    i = 2
    while n >1:
        if n % i == 0:
            n = n / i
        else:
            i = i + 1
    return largest_prime_factor
