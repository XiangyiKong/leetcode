#!/usr/bin/python
def KMPSearch:
	M = len(pat)
	N = len(txt)

	#create lps[] that will hold the longest prefix suffix
	lps = [0]*M
	j = 0 # index for pat[]

	computeLPSArray(pat, M, lps)

	i=0 # index for txt[]
	while i<N:
		if pat[j]==txt[i]:
			i+=1
			j+=1
		if j==M:
			print 'Found pattern at index' + str(i-j)
		
		#mismatch after j matches
		elif i<N and pat[j] != txt[i]:
			# do not match lps[0..lps[j-1]] characters, 
			# they will match anyway
			if j!=0
				j = lps[j-1]git@github.com:XiangyiKong/leetcode.git
			else:
				i+=1

def computeLPSArray(pat, M, lps):
	len = 0 #length of the previous longest prefix suffix

	lps[0] #lps[0] is always 0
	i=1 #index i pat[i]

	# the loop calculate lps[i] for i=1 to M-1
	while i<M:
		# match
		if pat[i]==pat[len]:
			len+=1
			lps[i]=len
			i+=1
		# mismatch
		else:
			# yes, find another possible match backwards
			if len!=0:
				len = lps[len-1]
			# no, no possible match
			else:
				lps[i]=0
				i+=1

















