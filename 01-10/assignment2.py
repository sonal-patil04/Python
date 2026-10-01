#2] Accept two values S and N. Print square of first N numbers staring from s
s=int(input("Enter a number: "))
n=int(input("Enter a number: "))

for i in range(s,s+n):
    print(i*i)