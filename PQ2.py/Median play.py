__author__ = 'jfung'

import numpy
import statistics

# Save ints to array
list = []
intList = []
with open('QuickSort.txt', 'r') as f:
    list = f.read().splitlines()
    intList = [int(c) for c in list]
f.close()

def set(x):
    global globalCount
    globalCount += (x-1)

globalCount = 0

def quickSort(arr, start, end):
    if start < end:
        split = partition(arr, start, end)
        #recurse around sorted pivot
        quickSort(arr, start, split)
        quickSort(arr, split + 1, end)


def partition(array, start, end):
    if len(array[start:end]) > 2:
        pivot = findMedian(array, start, end)
    else:
        pivot = start
    if pivot != start:
        array[pivot], array[start] = array[start], array[pivot]
    #update count
    length = len(array[start:end])
    set(length)
    i = start + 1
    pivotVal = array[start]
    for j in range(i, end):
        if array[j] < pivotVal:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[start], array[i-1] = array[i-1], array[start]
    return i-1




def findMedian(arr, start, end):
    cutArray = arr[start:end]
    midpt = len(arr[0:start]) + (len(cutArray)-1)//2
    medianArray = [arr[start], arr[midpt], arr[end-1]]
    median = statistics.median(medianArray)
    if median == arr[start]:
        pivot = start
    elif median == arr[end-1]:
        pivot = end-1
    else:
        pivot = midpt
    return pivot

quickSort(intList, 0, len(intList))
print globalCount
