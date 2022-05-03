fh = open("f:\\list.txt","r")
word = input("Enetr the word to Search")

n= len(word)

j=0
count = 1
L= fh.readlines()

for i in L:
    if (i.startswith(word)):
        print("Line number ",count,":",i)
    count +=1
