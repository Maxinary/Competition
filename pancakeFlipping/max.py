from random import shuffle

count = 0
def flip(lis, index):
	global count
	count+=1
	return lis[:index]+lis[index:][::-1]

def getNextLargest(s,k):
	if k in s[:len(s)-1]:
		return s[s.index(k)+1]
	return None

def rIndex(ar, element):
	index = -1
	for i in range(len(ar)):
		if ar[i]==element:
			index = i
	return index

def swapToClose(lis, index, s):
	#move to the top
	if index != len(lis)-1:
		lis = flip(lis, index)
	if getNextLargest(s,lis[index]) != None:
		lis = flip(lis,rIndex(lis,getNextLargest(s,lis[index]))+1)
		lis = flip(lis,rIndex(lis,getNextLargest(s,lis[index]))+2)
	else:#move to bottom, lowest element
		lis = flip(lis,0)
		lis = flip(lis,1)
	return lis

def panSort(lis):
	sorted = False
	s = list(set(lis))
	while sorted==False:
		for i in range(len(lis)-1,-1,-1):#iterate backwards
			if i==0:#sorted
				sorted = True
			elif lis[i-1] != getNextLargest(s,lis[i]) and lis[i-1] != lis[i]:
				lis = swapToClose(lis, i, s)
				break;
		print(count)
		print("\t",lis)
	return lis

if __name__ == "__main__":
	k = list(range(10))*2
	shuffle(k)
	k = k[:10]
	panSort(k)
