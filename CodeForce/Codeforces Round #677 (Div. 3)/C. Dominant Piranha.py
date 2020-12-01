# Python program for implementation of heap Sort 

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
	largest = i # Initialize largest as root 
	l = 2 * i + 1	 # left = 2*i + 1 
	r = 2 * i + 2	 # right = 2*i + 2 

	# See if left child of root exists and is 
	# greater than root 
	if l < n and arr[i] < arr[l]: 
		largest = l 

	# See if right child of root exists and is 
	# greater than root 
	if r < n and arr[largest] < arr[r]: 
		largest = r 

	# Change root, if needed 
	if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i] # swap 

		# Heapify the root. 
		heapify(arr, n, largest) 

# The main function to sort an array of given size 
def heapSort(arr,length):
	n = length

	# Build a maxheap. 
	for i in range(n//2 - 1, -1, -1): 
		heapify(arr, n, i) 

	# One by one extract elements 
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] # swap 
		heapify(arr, i, 0) 

# Driver code to test above
for _ in range(int(input())):
    n=int(input())
    a =list(map(int,input().split()))
    arr=a.copy()
    heapSort(arr,n)

    if(arr[0]==arr[n-1]):
        print(-1)
    else:
        if(a[0]==arr[n-1] and a[0]>a[1]):
            print(1)
        elif(a[n-1]==arr[n-1] and a[n-1]>a[n-2]):
            print(n)
        else:
           
            for i in range(1,n-1):

                if(a[i]==arr[n-1] and (a[i]>a[i+1] or a[i]>a[i-1]) ):
                    print(i+1)
                    break
