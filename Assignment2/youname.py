#print exercises

print('j')
print('o')
print('l')
print('i')
print('e')
#2. No variables show up in the variable editor. This is because no variables were assigned. 


#Operation exercises 

print(5/2)
print(5.0/2.0)
#python outputs the same value for these operations
print(5%2)
print(10%6) 
print(7%11)
#the modulo operator(%) gives the remainder of division 
print(5**2)
print(10**6)
print(7**11)
#the (**) operator does exponentation 
print(5//2)
print(10//6)
print(7//11)
#the (//) operator does division and gives us the whole number rounded down 
print(5+2+10*6/7)
print(5+2+(10*(6/7)))
print(24+7+10*15/4)
print(24+7+(10*(15/4)))
#python does follow order of operations.


#variable exercises
letter1='j'
letter2='o'
letter3='l'
letter4='i'
letter5='e' 
#yes, all 5 of the variables show up in the variable editor 
letterX='j'
print(letter1)
print(letterX)
#no, python does not hae a problem with two different variables having the same value
letterX='a'
print(letterX)
print(letter1)
#changing the value of letterX only changed the value of letterX
letterX=letter1
print(letterX)
print(letter1)
letter1='z'
print(letterX)
print(letter1)
#no, changing the value of letter1 did not change the value of letterX
#this tells us that python variable assignment works in order, changing the value of letter1 means that letterX=letter1 is no longer viable 


#boolean exercises
print(1==1.0)
#yes '1' and 1.0' are equivalent, this is becausethey represent the same number 
print(5==(3+2))
#yes 5 and (3=2) are equivalent, represent same number
print(1==1.0 and 1==1.0 or 5==(3+2))
print(1==1.0 and 1==1.0 and 5==(3+2))
print(1==1.0 or 1==1.0 or 5==(3+2))
print(1==1.0 or 1==1.0 or not 5==(3+2))
print(1==1.0 or 1==1.0 and 5==(3+2))


#list exercises
oddlist=[1,3,5,7,9]
#yes, oddlist became a variable 
print(oddlist)
print(len(oddlist))
#when you use len function on oddlist, python says the length is 5 
print(type(oddlist))
#when you use the type function on oddlist, python says it is a lsit
intlist=range(100)
print(list(intlist))
#yes it lists all integers between 0 and 100


#dictionary exercises
foods=['sushi', 'noodles', 'cheesecake']
name=['jolie']
age=['22.0']
year=['5']
about_me={'yourname':name, 'age':age, 'year of study':year, 'favourite foods':foods}
print(about_me)
print(type(about_me))
print(len(about_me))
#python determines the lengh of dictionary by the number of variables represented, for example about_me is 4


#array exercises 
import numpy
mixnums=numpy.array([5,6,7,2.25,3.25,4.25])
print(mixnums)
print(type(mixnums))
#the array has turned all the integers into floats 
mixtypes=numpy.array([5,6,2.25,3.25,'happy','love'])
print(mixtypes)
print(type(mixtypes))
#the array has turned all te value into strings
#python tries to make arrays in mixed types to be the same type
oddarray=numpy.array([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99])
print(oddarray)
print(type(oddarray))
import numpy as np
print(np.logspace(1,5,16))