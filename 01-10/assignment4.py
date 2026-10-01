#4] Accept sentence from user and count the vowels
a=input("Enter your sentence: ")
count=0
vowels="aeiouAEIOU"

for i in a:
    if i in vowels:
        count=count+1
print(count)