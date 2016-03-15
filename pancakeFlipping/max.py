from random import shuffle

''' 
NOTE: Currently only sorts lists which have the characteristics of shuffle(range(n)) where n is an int
'''
count = 0
def flip(lis, index):
	global count
	count+=1
	return lis[:index]+lis[index:][::-1]

def swapToClose(lis, index):
	#move to the top
	lis = flip(lis, index)
	if lis[index]-1 in lis[:len(lis)-1]:
		#print("moving",lis[index]+1,"next to",lis[index])
		lis = flip(lis,lis.index(lis[index]-1)+1)
	else:#move to bottom, lowest element
		lis = flip(lis,0)
		lis = flip(lis,1)
	return lis

def panSort(lis):
	sorted = False
	while sorted==False:
		for i in range(len(lis)-1,-1,-1):#iterate backwards
			if i==0:#sorted
				sorted = True
			elif lis[i]-lis[i-1] != 1:
				lis = swapToClose(lis,i)
				break;
		print(count)
		print("\t",lis)
	return lis

k = list(range(5))
shuffle(k)
panSort(k)
