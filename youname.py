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