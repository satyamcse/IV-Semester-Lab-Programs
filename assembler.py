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
		startaddress = int(li[2])
		output_table.append([""]+li) if len(li)==3 else output_table.append(["","**"]+li)
	else:
		offset_fix = 0
		if len(li)==3 and li[0]!='**':
			symbol = li[0]
			if symbol in symbol_table:
				print("PASS1 Failed!")
				exit (0)
			symbol_table[symbol]=startaddress+offset
			if (li[1]=='RESW'):
				offset_fix = 3*int(li[2]) - 3
			elif li[1]=='RESB':
				offset_fix = int(li[2]) - 3
			elif li[1]=='BYTE':
				offset_fix = len(li[2]) - 3 - 3
		output_table.append([startaddress+offset]+li)if len(li)==3 else output_table.append([startaddress+offset,"**"]+li)
		offset+=3+offset_fix
print("Symbol Table")
for i in symbol_table.keys():
	print(i, symbol_table[i])
print("\nOutput Table")
for j in output_table:
	print(j)
