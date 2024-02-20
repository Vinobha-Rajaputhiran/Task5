input="Guvi Geeks Network Private Limited"

val1=val2=val3=val4=val5=0

for x in input:
    if x=='a':
        val1=val1+1
    elif x=='e':
        val2=val2+1
    elif x == 'i':
        val3=val3+1
    elif x=='o':
        val4=val4+1
    elif x=='u':
        val5=val5+1

print ("The vowel values in the given statement are as below:")
print('a=', val1)
print('e=', val2)
print('i=', val3)
print('o=',val4)
print('u=', val5)