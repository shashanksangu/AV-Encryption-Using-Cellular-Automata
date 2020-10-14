from PIL import Image
import numpy as np
import time
import os



def fne(st):
	# Rule 15 of Cellular Automata
	for c in range(4):
		tmp = ''
		a = int(st[-1])
		a = 0 if a==1 else 1
		tmp = tmp + str(a)
		for i in range(1,8):
			a = int(st[i-1])
			a = 0 if a==1 else 1
			tmp = tmp + str(a)
		st = tmp[:]
	return st

def main():
	dte = dict()
	for i in range(256):
		st = f"{i:b}"
		while len(st)!=8 :
			st = '0' + st
		dte[i]=(int(fne(st),2)*187)%256
	#print(dte)
	#print("\n\n\n")
	
	ct = 0

	try:
    		if not os.path.exists('Enc'):
        		os.makedirs('Enc')
	except OSError:
   		print ('Error: Creating directory of data')

	while(1):	

		name = './data/frame'+str(ct) +'.png'
		img = Image.open(name)
		arr = np.array(img)
		arrMod = np.array(img)

		img = Image.fromarray(arr)

		print("-->"+str(ct))

		for i in range(480):
			for k in range(848):
				for l in range(3):
					arrMod[i,k,l]=dte[arr[i,k,l]]
				#arrMod[i,k]=dte[arr[i,k]]

		img = Image.fromarray(arrMod)
		name1 = './Enc/frame'+str(ct) +'.png'	
		img.save(name1)	
		ct = ct + 1

if __name__== "__main__":
	st = time.time()
	main()
	print(time.time()-st)
