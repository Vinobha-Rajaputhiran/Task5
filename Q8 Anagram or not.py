input1= str(input("Enter first string: "))
input2= str(input("Enter first string: "))

print("Are the two given strings Anagrams? ", end="")

if (sorted(input1) == sorted(input2)):
        print("True")
else:
        print("False")

