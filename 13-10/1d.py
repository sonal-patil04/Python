# Read a file, split its content into words, and store them in a list.
# i] Print the total number of words.

with open ("a.txt", "r") as f:
    data =f.read()

    words = data.split()

    print("Total words: ", len(words))





# ii] Print all unique words.

with open("a.txt", "r") as f:
    data = f.read()

words=data.split()
unique=[]

for word in words:
    if word not in unique:
        unique.append(word)

print("Unique words: ", unique)
