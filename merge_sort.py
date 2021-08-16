# Python program for implementation of MergeSort
class MergeSort:
	def __init__(self,arr):
		self.arr = arr
		
	def mergeSort(self,arr):
		if len(arr) > 1:
			mid = len(arr)//2
			L = arr[:mid]
			R = arr[mid:]
			self.mergeSort(L)
			self.mergeSort(R)
			i = j = k = 0
			while i < len(L) and j < len(R):
				if L[i] < R[j]:
					arr[k] = L[i]
					i += 1
				else:
					arr[k] = R[j]
					j += 1
				k += 1
			while i < len(L):
				arr[k] = L[i]
				i += 1
				k += 1

			while j < len(R):
				arr[k] = R[j]
				j += 1
				k += 1
	def printList(self,arr):
		for i in range(len(arr)):
			print(arr[i])


# Driver Code
if __name__ == '__main__':
	arr = [98,32,76,43,23]
<<<<<<< HEAD
	print("Given array is \n")
	merge = MergeSort(arr)
	merge.printList(arr)
	merge.mergeSort(arr)
	print("Sorted array is:\n")
	merge.printList(arr)
=======
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)
#output- 23,32,43,76,98
>>>>>>> 58c634613cc85f03e4609d7c106f5b0f21845545
