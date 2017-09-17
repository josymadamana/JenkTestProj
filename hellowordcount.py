## Open file and cound the number of occurance of the word "Hello" without any case check##
foundFlag=0
file=open("file.txt","r")
for word in file.read().split():
    if(word.lower() == 'hello'):
	foundFlag=1
	break
if(foundFlag):
    print "YES"
else:
    print "NO"
