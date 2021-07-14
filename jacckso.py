
yourName = 'jack'

myName = yourName

print len(myName)

myName = "jackson"


print len(myName)

myName = [1000,20,401]

for num in myName:

    num1 = num + 20

    numStr = "%d%d" % (num, num+1)
    numStr1 = int(numStr) + 20

    print "numStr1:%d" % (numStr1)
    #print len(numStr)

print len(myName)

print yourName
print myName

