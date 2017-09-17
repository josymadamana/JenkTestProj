## Open file and cound the number of occurance of the word "Hello" without any case check##
file=open("file.txt","r")
for word in file.read().split():
    if(word.lower() == 'hello'):
        print "YES"
    else
        print "NO"
