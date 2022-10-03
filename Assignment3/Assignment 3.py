#Variable Operations Exercises
sub_code='sub'
subnr_int=2
subnr_str='2'
print(sub_code+subnr_str)
print(sub_code+subnr_int)
#the str format can be added to sub_code to create sub2
#these both don't work because only strings can be added together and sub_itn is in integer form
print (sub_code+" "+subnr_str)
print(sub_code+" "+subnr_str*3)
print((sub_code+subnr_str)*3)
print((sub_code*3)+(subnr_str*3))


#List Operation Exercise
numlist=[1,2,3]
print(numlist*2)
import numpy
data=numpy.array([1,2,3])
print(data*2)
#when multiplying lists, python repeats the numbers twice, when multiplying arrays, python multiplies each value by 2
strlist=['do','re','mi','fa']
X=strlist[0]
Y=strlist[1]
Z=strlist[2]
K=strlist[3]
strlists=X*2,Y*2,Z*2,K*2
print(strlists)
print(strlist*2)
strlist.insert(1,'do')
strlist.insert(3,'re')
strlist.insert(5,'mi')
strlist.insert(7,'fa')
print(strlist)
strlist=['do','re','mi','fa']
print(list(zip(strlist,strlist)))

#Zipping Exercises
faces=['face1.png']*5+['face2.png']*5+['face3.png']*5+['face4.png']*5+['face5.png']*5+['house1.png']*5+['house2.png']*5+['house3.png']*5+['house4.png']*5+['house5.png']*5
house=['house1.png','house2.png','house3.png','house4.png','house5.png']*5+['face1.png','face2.png','face3.png', 'face4.png','face5.png']*5
postcue=['cue1']*25+['cue2']*25
memory=list(zip(faces,house,postcue))
import numpy as np
np.random.shuffle(memory)
print(memory)
print(len(memory))


#Indexing Exercises
colors=['red','orange','yellow','green','blue','purple']
print(colors[-2])
print(colors[-2][2])
print(colors[-2][3])
colors.remove('purple')
colors.insert(5,'indigo')
colors.insert(6,'violet')
print(colors)


#Slicing Exercises
list100=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100)
print(list100[ :10])
print(list100[98: :-2])
print(list100[99:94:-1])
print(list100[40:44])
print((list100[40:44])==(39,40,41,42,43))
#this is false
