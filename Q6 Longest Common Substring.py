input1 = input('Enter the first string: ')
input2 = input('Enter the second string: ')
answer = ""
len1, len2 = len(input1), len(input2)
for i in range(len1):
    for j in range(len2):
        temp=0
        match = ''
        while ((i+temp < len1) and (j+temp<len2) and   input1[i+temp] == input2[j+temp]):
            match = match+ input2[j+temp]
            temp = temp+1
        if (len(match) > len(answer)):
            answer = match

print("The longest common substring is: ", answer)