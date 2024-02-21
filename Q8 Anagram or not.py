input1= str(input("Enter first string: "))
input2= str(input("Enter second string: "))

print("Are the two given strings Anagrams? ", end="")

if (sorted(input1) == sorted(input2)): #counter() function can also be used
        print("True")
else:
        print("False")

