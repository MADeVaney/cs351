from random import randint
import time

A = [randint(-1000,1000) for i in range(1000)]
B = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]



def max_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low+high)//2
        (leftlow, lefthigh, leftsum) = max_subarray(A, low, mid)
        (rightlow, righthigh, rightsum) = max_subarray(A, mid+1, high)
        (crosslow, crosshigh, crosssum) = max_crossing_subarray(A, low, mid, high)
        if leftsum >= rightsum and leftsum >= crosssum:
            return(leftlow, lefthigh, leftsum)
        elif rightsum >= leftsum and rightsum >= crosssum:
            return(rightlow, righthigh, rightsum)
        else:
            return (crosslow, crosshigh, crosssum)
        
def max_crossing_subarray(A, low, mid, high):
    leftsum = float('-inf')
    sum = 0
    maxleft = 0
    maxright = 0
    for i in range(mid, low, -1):
        sum = sum + A[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
    rightsum = float('-inf')
    sum = 0
    for i in range(mid + 1, high):
        sum = sum + A[i]
        if sum > rightsum:
            rightsum = sum
            maxright = i
    return (maxleft, maxright, leftsum + rightsum)

def max_subarray_brute(A):
    n = len(A)
    max = float('-inf')
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum = sum+A[j]
            if sum > max:
                max = sum
                low = i
                high = j
    return(low,high, max)

def max_subarray_linear(A):
    n = len(A)
    max = float('-inf')
    endsum = float('-inf')
    for j in range(n):
        endhigh = j
        if endsum > 0:
            endsum = endsum + A[j]
        else:
            endlow = j
            endsum = A[j]
        if endsum > max:
            max = endsum
            low = endlow
            high = endhigh
    return (low, high, max)

print("Random sequence of 1000: ")

print("Divide and conquer")
divide1 = time.time()
print(max_subarray(A, 0, 999))
divide2 = time.time()
print(divide2 - divide1)

print("Brute force")
brute1 = time.time()
print(max_subarray_brute(A))
brute2 = time.time()
print(brute2 - brute1)

print("Linear")
linear1 = time.time()
print(max_subarray_linear(A))
linear2 = time.time()
print(linear2 - linear1)

print("Book example: ")

print("Divide and conquer")
divide1 = time.time()
print(max_subarray(B, 0, 15))
divide2 = time.time()
print(divide2 - divide1)

print("Brute force")
brute1 = time.time()
print(max_subarray_brute(B))
brute2 = time.time()
print(brute2 - brute1)

print("Linear")
linear1 = time.time()
print(max_subarray_linear(B))
linear2 = time.time()
print(linear2 - linear1)