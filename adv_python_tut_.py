# -*- coding: utf-8 -*-

w = "welcome to home of aryan singh this is system based technology"

n = w.lower()
e = w.upper()
t = w.title()
m = w.capitalize()

print(n)
print(e)
print(t)
print(m)

print(w.find("a"))

print(w.find("e"))

print(w.find("e",4 )) #-----> to find a character staring from the specified character.


''' if we enter any chahrcter in the find command which is not in the
string , then it will return -1
'''

print(w.find("z")) # ---> Returns -1

'''index function also returns th index of the specified character in the
  string '''

a = "Hello , this is Aryan Singh. We are coding in python. "

print(a.find('l'))
print(a.index("l"))

# BOTH WILL RETURN 2


''' But in the case of index, if the specified character in not present
in the string, then it will throw an 'VALUE ERROR ' whereas in the find
command it return with result : -1 '''

'''
isaplha()---> Function return True when the string contains
only alphabets and return False when the string contains
other characters than alphabets.

'''
# For Example

er= "Hello,thisisAryanSinghfromVaranasi"
print(er.isalpha()) # ---> Returns 'FALSE ' because there is "," after Hello

wr= "HellothisisAryanSinghfromVaranasi"
print(wr.isalpha()) # ---> Returns "TRUE " as the wr contains only alphabet charcters.

'''
   isdigit() commands return True if the string contains all the digit characters
   whereas return False if the string contains characters other than digit.


'''

# For Example

# x = "Hello123"
# print(x.isdigit()) #--> Return False

h = 344556
print(h.isdigit()) #--> Return True

'''
isalnum() function returns true if the string either contains  alphabet, digit
or both.

'''
# For Example -

we = "Welcome345"

print(we.isalnum()) # will return TRUE

'''

chr() function converts the character's ASCII int value to ASCII character

'''
# For Example

a = 65
print(chr(a))

b = 66
print(chr(b))
print(chr(90))

print(chr(99))
print(chr(456))
print(chr(233))

'''
ord() converts ASCII character into its ASCII int value

'''

print(ord("Q"))
print(ord("A"))
print(ord("r"))
print(ord("y"))
print(ord("S"))
print(ord("w"))

'''
format() function is used to concatenate a character or string in
between the string



'''
#this can be done in many forms -

# namedindexes

w= "Welcome to {a} of {b}"
n = w.format(a ='World', b ='Coding')
print(n)


#numberedindexes

s = "Welcome to the {0} of {1}"
k = s.format('Home','Aryan')
print(s)
print(k)

# EmptyPlaceholders

d = "Welcome to {} of {}"
f = d.format("Office","Mr.Singh")

print(d)
print(f)

"""# LISTS"""

l = [23,34,45,56 , [87,76,54,54]] # nested list

# to get any character through the index of a nested list
# we can use

# FOE EXAMPLE ,WE HAVE TO GET 76 IN l
m = l[4][1]
print(m)

# To reverse the list

o = [12,4,56,43,54,76,978,70,65,85,64]
print(o[-1::-1])

# LIST ITERATION

for i in o:
  print(i)

print("_________________")
m = ['Aryan ', 34 ,56, 67, 'QWERTY', 'REDFT', 'ouinm']

for t in m :
  print(t)

#REVERSE LISTING
p = [23,45,56,67,78,89,90,98,87,675,65,543,32]
t = len(p)

for b in range(t-1, -1 , -1):
  print(p[b])

# LIST COMPREHENSION

# append --------->

k = []
for i in range (101):
  k.append(i)

print(k)

print(" ")

n = [m for m in range(101)]
print(n)

print(" ")

# Applying Filter

g = [h for h in range (201) if h%2==0]
print(g)

# List Functions
'''
del
pop()
remove()
clear()
'''

io = [ 123,234,345,456,567,678,789]
del io[2] # will delete list item on index 2
print(io)

y = [ 45,56,67,78]
y.pop(1)
print(y)


# remove(value)--> it takes value not index
r = [ 98,76,87,65,54]
r.remove(65)
print(r)

#clear()---> Clears full list

e = [i for i in range (23) if i %2 ==0 ]
print(e)
t = e.clear()
print(t , "The list is Empty ")

# UPDATE A ELEMENT FROM A LIST

w= [ 23,34,45,56,67,68]
print(w)
w[1]= 10
print(w)

# More List Functions
'''
insert()
append()
extends()

'''
# list.insert(position index , value )
m = [56,54,56,76]
print(m  )
m.insert(1,"Aryan")
print(m )

