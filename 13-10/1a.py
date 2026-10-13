# Write a program to read a file and count how many vowels are present in its content.

with open ("a.txt","r" ) as f:
    content = f.read()
    print(content)
    count = 0
    for i in content:
        if i in "aeiouAEIOU":
            count = count + 1
    print("Total vowels:", count)


