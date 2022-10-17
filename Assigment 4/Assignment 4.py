#Conditional Exercises
response1='1'
response2='2'
response3='NaN'
if response1=='1':
    print('OK')
elif response1=='1':
    print('Correct!')
if response2=='2':
    print('OK')
elif response2=='2':
        print('Incorrect!')
if response3=='NaN':
    print('subject did not respond')
else:print('subject pressed the wrong key')
#yes, it does what is expected


#For Loop Exercises 
letters=['J','o','l','i','e']
for letters in letters:
    if letters=='J':
        image='J'
    elif letters=='o':
        image='o'
    elif letters=='l':
        image='l'
    elif letters=='i':
        image='i'
    elif letters=='e':
        image='e'
    print(image)
letters=['J','o','l','i','e']
count=-1
for letters in letters:
    count =count+1
    if letters=='J':
        image='J'
    elif letters=='o':
        image='o'
    elif letters=='l':
        image='l'
    elif letters=='i':
        image='i'
    elif letters=='e':
        image='e'
    print(image)
    print('%i'%count)
names=['Amy','Rory','River']
for name in names:
   print(name)
   for letter in name:
       print(letter)
for name in names:
    counter=-1
    for letter in name:
        counter=counter+1
        print(letter)
        print(" " + str(counter))


#While Loop Exercises
time_counter=0 
while time_counter<20:
    if time_counter<10:
        print('image1.png%i'%time_counter)
    elif time_counter < 20:
        print('image2.png%i'% time_counter)
    time_counter=time_counter+1
import random
response=False
iteration=0
failsafe=-1
while not response:
    failsafe=failsafe+1
    if failsafe==5:
        break
    iteration=iteration+1
    print('Showing an image for %i iterations' %iteration)
    if random.randint(0,10) == 1:
        response=True 
    if random.randint(0,10)==2:
        response=True
iteration = 0 
while iteration < 20:
    if iteration < 10:
        print('%i, image1.png' % iteration)
    elif iteration < 20:
        print('%i, image2.png' % iteration)
    iteration = iteration + 1  



