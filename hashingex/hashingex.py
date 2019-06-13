import hashlib
import time

d = {}
d['208f1a0c208342372b75d914b6c098d626becf07'] = "??"#"500"
d['61fc7fbf6b24ff258633dad73f13f9bd66a2477f'] = "??"#"123456"
d['8a57a79d7a9921cd2344e7295dc72359780e9f9d'] = "??"#"121567"
d['bba1db3a9d5ba9f72b91312e730a9612dfdea053'] = "??"#"123456"
d['350d5bf1074e5557367a24ae9e07ab65aacfc031'] = "??"#"888888"
number1 = "208f1a0c208342372b75d914b6c098d626becf07" # created strings for each key
number2 = "61fc7fbf6b24ff258633dad73f13f9bd66a2477f"
number3 = "8a57a79d7a9921cd2344e7295dc72359780e9f9d"
number4 = "bba1db3a9d5ba9f72b91312e730a9612dfdea053"
number5 = "350d5bf1074e5557367a24ae9e07ab65aacfc031"
hex1 = "Not found" # created hex strings
hex2 = "Not found"
hex3 = "Not found"
hex4 = "Not found"
hex5 = "Not found"
num1 = 0 #integer containers for numbers
num2 = 0
num3 = 0
num4 = 0
num5 = 0
i = 1000000 #set the counter to 1 million
test = "" # created test and hashtest string containers
hashtest = ""
counter = 5
found1 = False #list of booleans created
found2 = False
found3 = False
found4 = False
found5 = False
while counter > 0: #while loops goes through all numbers 1 million through 0, the counter ensures that all five numbers are found
	test = "0x%X" % i # we convert the number to hex, we need both lower case and upper case
	test1 = "0x%x" % i
	hashtest = test.encode("utf-8") # we now encode our hex strings and then convert them to sha1
	hashtest = hashlib.sha1(hashtest).hexdigest()
	hashtest1 = test1.encode("utf-8")
	hashtest1 = hashlib.sha1(hashtest1).hexdigest()
	if hashtest == number1 or hashtest1 == number1 and found1 == False: #we now compare the sha strings to each of the 5 hashes we have
		if hex1 == "Not found": #If we find a match, we then change the hex string and number and add the number to the dictionary with the associated dictionary entry.
			if hashtest == number1:
				d[hashtest] = i
				hex1 = test
			elif hastest1 == number1:
				d[hashtest1] = i
				hex1 = test1
			print("found")
			num1 = i		
			counter-=1
			found1 = True
			i-=1
		continue
	elif hashtest == number2 and found2 == False:
		if hex2 == "Not found":
			d[hashtest] = i
			print("found")
			hex2 = test
			num2 = i
			counter-=1
			found2 = True
			i-=1
		continue
	elif hashtest == number3 or hashtest1 == number3 and found3 == False:
		if hex3 == "Not found":
			if hashtest == number3:
				d[hashtest] = i
				hex3 = test
			elif hashtest1 == number3:
				d[hashtest1] = i
				hex3 = test1
			print("found")
			num3 = i
			counter -=1
			found3 = True
			i-=1
		continue
	elif hashtest == number4 or hashtest1 == number4 and found4 == False:
		if hex4 == "Not found":
			if hashtest == number4:
				d[hashtest] = i
				hex4 = test
			elif hashtest1 == number4:
				d[hashtest1] = i
				hex4 = test1
			print("found")
			num4 = i
			counter -=1
			found4 = True
			i-=1
		continue
	elif hashtest == number5 or hashtest1 == number5 and found5 == False:
		if hex5 == "Not found":
			if hashtest == number5:
				d[hashtest] = i
				hex5=test
			elif hashtest1 == number5:
				d[hashtest1] = i
				hex5 = test1
			print("found")
			num5 = i 
			counter -=1
			found5 = True
			i-=1
		continue
	else:
		i-=1
	if i == 0: #This sets the counter back to 1 million if not all the 5 numbers are found
		i = 1000000
print ("COMPLETE") #Once all the numbers are found with print a complete statement

def putNumbersInOrder(): #This function orders all the numbers in the list
	list1 = [] 
	for n in d.keys(): #We first convert the dictionary to a list
		list1.append(d.get(n))
	counter = 0
	list1.sort() # We then use sort to arrange all the list items in order and return it
	return list1

print(hex1)
print(hex2)
print(hex3)
print(hex4)
print(hex5)
orderedlist = putNumbersInOrder()
print(orderedlist) #We out the printed list


