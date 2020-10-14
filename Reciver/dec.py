from PIL import Image
import numpy as np
import time
import os

def fnd(st):
	# Rule 85 of Cellular Automata
	for c in range(4):
		tmp = ''
		for i in range(7):
			a = int(st[i+1])
			a = 0 if a==1 else 1
			tmp = tmp + str(a)
		a = int(st[0])
		a = 0 if a==1 else 1
		tmp = tmp + str(a)
		st = tmp[:]
	return st

def main():
	
	
	dtd = dict()
	for i in range(256):
		g = (i*115)%256		
		st = f"{g:b}"
		while len(st)!=8 :
			st = '0' + st
		dtd[i] = int(fnd(st),2)
	#print(dtd)
	ct = 0
	try:
    		if not os.path.exists('Dec'):
        		os.makedirs('Dec')
	except OSError:
   		print ('Error: Creating directory of data')
	while(1):
		
		name = './Enc/frame'+str(ct) +'.png'
		img = Image.open(name)
		arrRev = np.array(img)
		print("-->"+str(ct))
		img = Image.fromarray(arrRev)
	
		for i in range(480):
			for k in range(848):
				for l in range(3):
					arrRev[i,k,l]=dtd[arrRev[i,k,l]]
				#arrRev[i,k]=dtd[arrRev[i,k]]

		img = Image.fromarray(arrRev)
		name1 = './Dec/frame'+str(ct) +'.png'
		img.save(name1)
		ct = ct + 1

if __name__== "__main__":
	st = time.time()
	main()
	print(time.time()-st)
