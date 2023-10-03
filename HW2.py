from random import randint
import time

def max_heapify(A, i, n):
    l = 2 * i
    r = (2 * i) + 1
    if l <= n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= n and A[r] > A[largest]:
        largest = r
    if largest != i:
        x = A[largest]
        A[largest] = A[i]
        A[i] = x
        A = max_heapify(A, largest, n)
    return A

def build_max_heap(A, n):
    for i in range(n//2, 0, -1):
        A = max_heapify(A, i, n)
    return A

def heapsort(A, n): #creates and maintains the sorted heap object
    A = build_max_heap(A, n)
    for i in range(n, -1, -1):
        x = A[0]
        A[0] = A[i]
        A[i] = x
        A = max_heapify(A, i, n)
    return A

'''def full_heapsort(A, n=0): #creates a list from lowest to highest
    n = len(A) - 1
    for i in range(n):
        A = build_max_heap(A[:n-i + 1], n-i) + A[n-i+1:]
        temp = A[n-i]
        A[n-i] = A[0]
        A[0] = temp
    return A'''

def check_heapsort(A2):
    for i in range(len(A2)):
        if A2[i] > A2[i//2]:
            print("Failed")


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    return A, i + 1

def quicksort(A, p ,r):
    if p < r:
        A, q = partition(A, p, r)
        A = quicksort(A, p, q - 1)
        A = quicksort(A, q + 1, r)
    return A

def check_sorted(A):
    for i in range(1, len(A) - 2):
        if A[i-1] > A[i] or A[i+1] < A[i]:
            print("failed")


# Testing on input sizes from homework

print("Heapsort")

time1 = time.time()
A = [randint(-1000,1000) for i in range(100)]
A2 = heapsort(A, 99)
time2 = time.time()
print("Time for 100 is: " + str(time2-time1))

time1 = time.time()
A = [randint(-1000,1000) for i in range(1000)]
A2 = heapsort(A, 999)
time2 = time.time()
print("Time for 1000 is: " + str(time2-time1))

time1 = time.time()
A = [randint(-1000,1000) for i in range(10000)]
A2 = heapsort(A, 9999)
time2 = time.time()
print("Time for 10000 is: " + str(time2-time1))

time1 = time.time()
A = [randint(-1000,1000) for i in range(100000)]
A2 = heapsort(A, 99999)
time2 = time.time()
print("Time for 100000 is: " + str(time2-time1))

print("Quicksort")

time1 = time.time()
A = [randint(-1000,1000) for i in range(100)]
A2 = quicksort(A, 0, 99)
time2 = time.time()
print("Time for 100 is: " + str(time2-time1))

time1 = time.time()
A = [randint(-1000,1000) for i in range(1000)]
A2 = quicksort(A, 0, 999)
time2 = time.time()
print("Time for 1000 is: " + str(time2-time1))

time1 = time.time()
A = [randint(-1000,1000) for i in range(10000)]
A2 = quicksort(A, 0, 9999)
time2 = time.time()
print("Time for 10000 is: " + str(time2-time1))

time1 = time.time()
A = [randint(-1000,1000) for i in range(100000)]
A2 = quicksort(A, 0, 99999)
time2 = time.time()
print("Time for 100000 is: " + str(time2-time1))
