import urllib2

#file = urllib2.urlopen('http://manning.com/sande2/date/message.txt')
file = urllib2.urlopen('http://txt2html.sourceforge.net/sample.txt')

message = file.read()
print message

# Python program to demonstrate
# writing to file

# Opening a file
file1 = open('myfile.txt', 'w')


# Writing multiple strings
# at a time
file1.writelines(message)

# Closing file
file1.close()