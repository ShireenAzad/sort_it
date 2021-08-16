# Python program for implementation of Insertion Sort
  
# Function to do insertion sort
class insertion:

    def __init__(self, arr, length):
        self.arr=arr
        self.length=length
    def insertionSort(self):
        print ("Sorted array is:")
    # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
    
            key = arr[i]
    
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >=0 and key < arr[j] :
                    arr[j+1] = arr[j]
                    j -= 1
            arr[j+1] = key
        for i in range(length):
            print(arr[i])
        
  
  
# Driver code to test above
arr = [12, 11, 13, 5, 6]
length=len(arr)
arr= insertion.insertionSort(arr)