input= str(input("Enter a string: "))
input2 = input.replace(' ', '') #removing space in given string
x= set(input2) #converting the string to set data type as set does not accept duplicate values
print('The number of unique character: ', len(x))