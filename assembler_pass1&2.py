try:
	file = open("ASSEMBLY.txt",'r')
except:
	print("File does not exist")
startaddress = -1
offset = 0	
symbol_table=dict()
output_table = []
for line in file:
	li = list(line.split())
	if startaddress==-1 and (li[1]=='START' or li[0]=='START'):
		startaddress = int(li[2],16)
		output_table.append([""]+li) if len(li)==3 else output_table.append(["","**"]+li)
	else:
		offset_fix = 0
		if len(li)==3 and li[0]!='**':
			symbol = li[0]
			if symbol in symbol_table:
				print("PASS1 Failed!")
				exit (0)
			symbol_table[symbol]=hex(startaddress+offset)
			if (li[1]=='RESW'):
				offset_fix = 3*int(li[2]) - 3
			elif li[1]=='RESB':
				offset_fix = int(li[2]) - 3
			elif li[1]=='BYTE':
				offset_fix = len(li[2]) - 3 - 3
		output_table.append([hex(startaddress+offset)]+li)if len(li)==3 else output_table.append([hex(startaddress+offset),"**"]+li)
		offset+=3+offset_fix
print("Symbol Table (HashMap)")
for i in symbol_table.keys():
	print(i, symbol_table[i])
print("\nOutput Table")
for j in output_table:
	print(j)
print ("Reading Optable...")
op_table = dict()
try:
	op = open("OpTable.txt",'r')
except:
	print("OpTable does not exist")
for line in op:
	li = line.split()
	op_table[li[0].upper()] = li[3]

print(op_table)
for li in output_table:
	if li[2]=='END':
		break
	elif li[2]=='START':
		continue
	else:
		operation = li[2]
		if operation not in op_table:
			if operation=="WORD":
				object_code = li[3]
			elif operation=="BYTE":
				object_code = li[3][2:len(li[3])-1]
			elif operation=="RESB" or operation=="RESW":
				object_code = " "
			else:
				print ("INVALID OPCODE ",operation,": Pass 2 failed!")
		else:
			object_code = op_table[operation]
			print(object_code)
			if len(li)>3:
				if li[3] not in symbol_table:
					print ("INVALID OPERAND ",li[3],": Pass 2 failed!")
				object_code= object_code + symbol_table[li[3]][2:]
			else: object_code+='0000'
		li.append(object_code)
print("\nOutput Table")
for j in output_table:
	print(j)
# TODO : Fix when Byte = c'F1' or x'F1'
