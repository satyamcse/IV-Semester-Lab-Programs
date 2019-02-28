try:
	file = open("ASSEMBLY.txt",'r')
except:
	print("File does not exist")
startaddress = -1
offset = 0	
symbol_table=dict()
output_table = []


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

index = 0
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
				for ind in symbol_table[symbol]:
					output_table[index][-1]+=hex(startaddress+offset)[2:]
				#print("PASS1 Failed!")
				#exit (0)
			symbol_table[symbol]=hex(startaddress+offset)
			if (li[1]=='RESW'):
				offset_fix = 3*int(li[2]) - 3
			elif li[1]=='RESB':
				offset_fix = int(li[2]) - 3
			elif li[1]=='BYTE':
				offset_fix = (len(li[2]) - 3 + 1)//2 - 3 if li[2][0]=='X' else (len(li[2]) - 3) - 3
		output_table.append([hex(startaddress+offset)]+li)if len(li)==3 else output_table.append([hex(startaddress+offset),"**"]+li)
		offset+=3+offset_fix
	li = output_table[-1]
	if li[2]=='END':
		break
	elif li[2]=='START':
		continue
	else:
		operation = li[2]
		if operation not in op_table:
			if operation=="WORD":
				li[3] = hex(int(li[3]))[2:]
				object_code = '0'*(6-len(li[3]))+li[3]
			elif operation=="BYTE":
				if "X'" in li[3]:
					object_code = li[3][2:len(li[3])-1]
				else:
					object_code = ""
					for i in list(li[3][2:len(li[3])-1]):
						object_code += str(hex(ord(i)))[2:]
			elif operation=="RESB" or operation=="RESW":
				object_code = " "
			else:
				print ("INVALID OPCODE ",operation,": Pass 2 failed!")
		else:
			object_code = op_table[operation]
			print(object_code)
			if len(li)>3:
				if ',X' in li[3]:
				 	li[3] = li[3][:len(li[3])-2]
				# 	k = symbol_table[li[3]][2:]
				# 	k = hex(int(k,16)+2**15)[2:]
				# else: k = symbol_table[li[3]][2:]
				if li[3] not in symbol_table:
					print ("Forward refernce for :",li[3]," : Pass 1")
					object_code = object_code
					symbol_table[li[3]] = [index]
				elif type(symbol_table[li[3]]) is list:
					print ("Forward refernce for :",li[3]," : Pass 1")
					object_code = object_code
					symbol_table[li[3]].append(index)
				else: object_code= object_code + symbol_table[li[3]][2:]
			else: object_code+='0000'
		li.append(object_code)
	index+=1
print("Symbol Table (HashMap)")
for i in symbol_table.keys():
	print(i, symbol_table[i])

print("\nOutput Table")
for j in output_table:
	print(j)
name = input("Program name?")
if len(name)>6:
	name= name[:6]
if len (name)<6:
	name = name+' '*(6-len(name))
s1 = 'H^'+name+'^00'+output_table[1][0][2:]+'^0000'+hex(offset-3)[2:]

s2 = 'T^00'+output_table[1][0][2:]+'^1E'
for i in output_table:
	try:
		if len(i)>4 and len(i[4])==6:
			s2+='^'+i[4]
	except:
		a=5

s3 = 'E^'+'00'+output_table[1][0][2:]
print(s1)
print(s2)
print(s3)
file = open("Output.txt",'w')
file.write(s1+'\n'+s2+'\n'+s3)
file.close()
