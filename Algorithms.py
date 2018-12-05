
import time
import math
from datetime import datetime


FACTOR = 1000000

class SortingAlg:
    array = []
    agthms = {'InsertionSort': {}, 'MergeSort': {}, 'QuickSort': {}}
    dicis = agthms['InsertionSort']
    dicms = agthms['MergeSort']
    dicqs = agthms['QuickSort']

    nis = 0
    tiis = 0
    tfis = 0

    nms=0
    tims=0
    tfms=0

    nqs = 0
    tiqs = 0
    tfqs = 0



    def insertionsort(A):
        j=1
        SortingAlg.tiis= time.time()*FACTOR
        for j in range (0,len(A)):
            SortingAlg.nis = SortingAlg.nis + 1
            if SortingAlg.nis % 10 == 0:
                SortingAlg.tfis = time.time()*FACTOR
                SortingAlg.agthms['InsertionSort'][SortingAlg.nis] = int(SortingAlg.tfis - SortingAlg.tiis)
            key=A[j]
            i=j-1
            while i>(-1) and A[i]>key:
                A[i+1]=A[i]
                i=i-1
            A[i+1]=key

    def mergeSort(alist):
        if SortingAlg.nms==0:
            SortingAlg.tims=time.time()*FACTOR
        if len(alist)==1:
            SortingAlg.nms=SortingAlg.nms+1
            if SortingAlg.nms % 10 == 0:
                SortingAlg.tfms=time.time()*FACTOR
                SortingAlg.dicms[SortingAlg.nms]=int(SortingAlg.tfms-SortingAlg.tims)

        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
            SortingAlg.mergeSort(lefthalf)
            SortingAlg.mergeSort(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i + 1
                else:
                    alist[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                alist[k] = righthalf[j]
                j = j + 1
                k = k + 1

    def quicksort(alist):
        SortingAlg.tiqs = time.time()*FACTOR
        SortingAlg.quickSortHelper(alist, 0, len(alist)-1)

    def quickSortHelper(alist, first, last):

        if(first==last):
            SortingAlg.nqs = SortingAlg.nqs + 1
            if SortingAlg.nqs % 10 == 0:
                SortingAlg.tfqs = time.time()*FACTOR
                SortingAlg.dicqs[SortingAlg.nqs] = int(SortingAlg.tfqs - SortingAlg.tiqs)

        if first<last:
            splitpoint = SortingAlg.partition(alist,first,last)
            SortingAlg.nqs = SortingAlg.nqs + 1
            if SortingAlg.nqs % 10 == 0:
                SortingAlg.tfqs = time.time()*FACTOR
                SortingAlg.dicqs[SortingAlg.nqs] = int(SortingAlg.tfqs - SortingAlg.tiqs)
            SortingAlg.quickSortHelper(alist,first,splitpoint-1)
            SortingAlg.quickSortHelper(alist,splitpoint+1,last)


    def partition(alist,first,last):
       pivotvalue = alist[first]

       leftmark = first+1
       rightmark = last

       done = False
       while not done:

           while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
               leftmark = leftmark + 1

           while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
               rightmark = rightmark -1

           if rightmark < leftmark:
               done = True
           else:
               temp = alist[leftmark]
               alist[leftmark] = alist[rightmark]
               alist[rightmark] = temp

       temp = alist[first]
       alist[first] = alist[rightmark]
       alist[rightmark] = temp

       return rightmark


    def reset():
        SortingAlg.array = []
        SortingAlg.agthms = {'InsertionSort': {}, 'MergeSort': {}, 'QuickSort': {}}
        SortingAlg.dicis = SortingAlg.agthms['InsertionSort']
        SortingAlg.dicms = SortingAlg.agthms['MergeSort']
        SortingAlg.dicqs = SortingAlg.agthms['QuickSort']

        SortingAlg.nis = 0
        SortingAlg.tiis = 0
        SortingAlg.tfis = 0

        SortingAlg.nms = 0
        SortingAlg.tims = 0
        SortingAlg.tfms = 0

        SortingAlg.nqs = 0
        SortingAlg.tiqs = 0
        SortingAlg.tfqs = 0