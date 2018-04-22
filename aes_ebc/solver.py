from pwn import *
import string
from sys import *
cocok = string.printable
"""
flag
flag{rem3mber_th e_pic_of_tux_aes 
flagflagflagflag flagflagflagflag flagflagflagflag
55301be4d2dae6a335c73df2f4b46032 55301be4d2dae6a335c73df2f4b46032 55301be4d2dae6a335c73df2f4b46032
"""

p = process(["python", "soal.py"])

flag = ""
x = 0

for i in range(0, 16):
	print i, flag
	for j in cocok:
		pload =  "A" * (32 - len(flag) - 1)
		pload += flag + j + "A" * (16 - len(flag) - 1)
		p.sendline(pload)
		hasil = p.recv(1000)
		if(hasil[0:32] == hasil[64:64+32]):
			flag += j
			x = i
			break
			# print hasil[0:32] , hasil[64:64+32]
			# print pload
			# print flag

m = x
flag2 = ""
for i in range(m, m+16):
	print i, flag
	for j in cocok:
		pload =  "A" * (32 - len(flag) - 1)
		pload += flag2 + j + "A" * (16 - len(flag2) - 1)
		p.sendline(pload)
		# print pload
		hasil = p.recv(1000)
		if(hasil[32:64] == hasil[64:64+32]):
			flag += j
			flag2 += j
			x = i
			break

flag3 = ""
m = x 
for i in range(m, m+16):
	print i, flag
	pload =  "A" * (16 - len(flag3) - 1)
	p.sendline(pload)
	dapet = p.recv(1000)[64:64+32]
	for j in cocok:
		pload =  j + "A" * (16 - len(flag3) - 1)
		p.sendline(pload)
		tebak = p.recv(1000)[64:64+32]
		if(dapet == tebak):
			flag += j
			flag3 += j
			x = i
			break
