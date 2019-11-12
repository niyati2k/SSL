fl=0
try:
	pin=int(input("Enter the pin: "))
	if(pin==4949):
		print("Lock Opened")
		fl=1
	elif(pin>9999 or pin<0):
		exit()
		# exit()
	else:
		print("Wrong PIN! Try again")
	pass
except:
	print("Full alarm")
	exit()
if(fl==1):
	exit()

try:
	pin=int(input("Enter the pin: "))
	if(pin==4949):
		print("Lock Opened")
	else:
		print("Full alarm")
	pass
except:
	print("Full alarm")