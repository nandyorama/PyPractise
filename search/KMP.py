

def lpsarray(pat,n,lps):
	i = 1
	j = 0
	lps[0] = 0
	while i < n:
		if pat[i] == pat[j]:
			j += 1
			lps[i] = j
			i += 1
		else:
			if j != 0:
				j = lps[j-1]
			else:
				lps[i] = 0
				i += 1
				

def kmp(txt,pat):
	n = len(pat)
	m = len(txt)
	lps = [0] * (n)
	lpsarray(pat,n,lps)#create/fill lps array 
	#for i in lps:
	#	print(i)
	i = j = 0
	while i < m:
		if pat[j] == txt[i]:
			i += 1
			j += 1
		if j == n:
			print("Pattern Found "+ str(i-j))
			j = lps[j-1]
		elif (i < m) and (pat[j] != txt[i]):
			if j != 0:
				j = lps[j-1]
			else:
				i += 1	 			

 
	
txt = "baababa"
pat = "abab"
kmp(txt,pat)
