print('Lova pizza!')

first_name = 'Bro'
last_name = 'Code'
full_name = first_name + '' + last_name
#print(type(full_name))
print('Hello '+full_name)

age = 21
age += 1

print("Youe age is: "+str(age))

#Multiple assignment

name, age, attraction = 'Bro', 21, True

Spanchbob = 30
Sandy = 30
Ploot = 30
Spanchbob = Sandy = Ploot = 30

#string methods
name = 'Bro Code'

print(name.find('B')) #find letter number
print(name.capitalize()) #Capitalize 1st symbol
print(name.upper()) #Capitalize all
print(name.lower()) #lower all
print(name.isdigit()) #Check for integer
print(name.isalpha()) #check string for only letters
print(name.count('o')) #how many 'o' includes
print(name.replace('o', 'a')) #replace 'o' for 'a'
print(name*3) #prints name 3 times

#type casting = convert data type in another data
x = 1
y = 2.0
z = '4'

#y = int(y)

print(float(x))
print(int(y))
print(int(z)*3)
print('X is a: '+str(x)) #method to convert int to str

#input functions
name = input('What is your name?: ')
age = int(input('How old are you?: '))
height = float(input('How tall are you?: '))


print('Hello, '+name)
print('You are '+str(age)+' years old') #convert int to str
print('Tou are '+str(height)+' cm tall')