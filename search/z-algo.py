
def search(txt,pat):
	res = pat + '$' + txt
	n = len(res)
	print("length of final string "+ res +"---"+ str(n))
	L = R = 0
	i = 1
	z = [0] * len(res) #The * operator can be used as [object]*n where n is the no of elements in the array.
	z[0] = len(res)

	for i in range(1,n):
		if i > R:
			L = R = i
			while R < n and res[R-L]==res[R]:
				R += 1
			z[i] = R-L
			R -= 1
		else:
			k = i - L
			if z[k]<R-i+1:
				z[i] = z[k]
			else:
				L = i
				while R < n and res[R-L]==res[R]:
					R += 1
				z[i] = R - L
				R -= 1
		i += 1
	print(z)	
	
	for ii in z:
		#print(ii)
		if ii == len(pat):
			print("Found at index "+str(ii-len(pat)+1)) 
	
txt = "baaba"
pat = "aab"
search(txt,pat)
