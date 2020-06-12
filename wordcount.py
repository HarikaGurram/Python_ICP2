file=open("Input.txt","r+")   #opening a file in write and read mode
wordcount={}                  #creating a dict
for word in file.read().split():   #spliting input data
    if word not in wordcount.keys():  # hecking if word  present in wordcount dict
        wordcount[word] = 1           #if not present value is 1
    else:
        wordcount[word] += 1          #if present value keeps on icreasing

for word in wordcount:                # for each key in wordcount printing out the values
    print (word,wordcount[word])
    
for key in list(wordcount.keys()):    # for each key in wordcount, writing the output into same file
    x=key + str(wordcount[key])
    file.write(x)
    file.write("\n")     

file.close()  #closing the file

