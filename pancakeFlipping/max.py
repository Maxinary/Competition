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
	v = lis[index]
	g = getNextLargest(s,v)
	if index != len(lis)-1:
		lis = flip(lis, index)
	if getNextLargest(s,lis[index]) != None:
		lis = flip(lis,rIndex(lis,g)+1)
		if rIndex(lis, v) == len(lis)-1:
			lis = flip(lis,rIndex(lis,g)+2)
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
				#print("moving: ",lis[i],",", getNextLargest(s,lis[i]))
				lis = swapToClose(lis, i, s)
				break;
		#print(count)
		#print("\t",lis)
	return lis

def panSimpleSort(lis):#efficiency: 3xlen(lis)
	s = list(set(lis))[::-1]
	elements = -1
	for i in range(len(s)):
		while rIndex(lis,s[i]) > elements:
			elements+=1
			if rIndex(lis,i) != len(lis)-1:
				lis = flip(lis, rIndex(lis,s[i]))
			if elements != len(lis)-1:
				lis = flip(lis,elements)
			#print(count)
			#print("\t",lis)
			
	print(count)

if __name__ == "__main__":
	tNums = [0,0]
	kNums = [0,0]
	for i in range(32):
		count = 0
		k = list(range(20))
		shuffle(k)
		panSort(k)
		tNums[0]+= count
		tNums[1]+=1
	for i in range(32):
		count = 0
		k = list(range(20))*2
		shuffle(k)
		k = k[:20]
		panSort(k)
		kNums[0] += count
		kNums[1] += 1
	print("tNums AVG", tNums[0]/tNums[1])
	print("kNums AVG", kNums[0]/kNums[1])
	
