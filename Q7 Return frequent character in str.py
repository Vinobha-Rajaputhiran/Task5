input= str(input("Enter your string: "))
input1=list(input.replace(" ",""))

print("The most common character in the string is: ", end="")

from collections import Counter #counter function is used to find the frequency of each character
ordered= Counter(input1)
print(ordered.most_common(1)[0][0]) #The first aka highest value is taken