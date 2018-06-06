#opening a file for word count
file=open('test_data.txt','r')

#creating a empty dictionary
dict={}
count=0

#processing data line by line
for line in file:
    #processing data word by word
    for word in line.split():
        #checks if word is in dictionary or not
        if word not in dict.keys():
            dict.update({word:count+1})
        else:
            #gets the current count of the given word
            old_count=dict.get(word)
            dict.update({word:old_count+1})
print(dict)
