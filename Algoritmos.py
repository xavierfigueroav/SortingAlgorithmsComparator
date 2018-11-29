
import time
import math
from datetime import datetime

class SortingAlg:
    nis = 0
    dicis = {}
    tiis = 0
    tfis = 0

    nms=0
    dicms={}
    tims=0
    tfms=0

    nqs = 0
    dicqs = {}
    tiqs = 0
    tfqs = 0

    nsts = 0
    dicsts = {}
    tists = 0
    tfsts = 0

    def insertionsort(A):
        j=1
        SortingAlg.tiis= time.time()*1000
        for j in range (0,len(A)):
            SortingAlg.nis = SortingAlg.nis + 1
            if SortingAlg.nis % 10 == 0:
                SortingAlg.tfis = time.time()*1000
                SortingAlg.dicis[SortingAlg.nis] = int(SortingAlg.tfis - SortingAlg.tiis)
            key=A[j]
            i=j-1
            while i>(-1) and A[i]>key:
                A[i+1]=A[i]
                i=i-1
            A[i+1]=key

    def mergeSort(alist):
        if SortingAlg.nms==0:
            SortingAlg.tims=time.time()*1000
        if len(alist)==1:
            SortingAlg.nms=SortingAlg.nms+1
            if SortingAlg.nms % 10 == 0:
                SortingAlg.tfms=time.time()*1000
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
        SortingAlg.tiqs = time.time()*1000
        SortingAlg.quickSortHelper(alist,0,len(alist)-1)

    def quickSortHelper(alist,first,last):

        if(first==last):
            SortingAlg.nqs = SortingAlg.nqs + 1
            if SortingAlg.nqs % 10 == 0:
                SortingAlg.tfqs = time.time()*1000
                SortingAlg.dicqs[SortingAlg.nqs] = int(SortingAlg.tfqs - SortingAlg.tiqs)

        if first<last:
            splitpoint = SortingAlg.partition(alist,first,last)
            SortingAlg.nqs = SortingAlg.nqs + 1
            if SortingAlg.nqs % 10 == 0:
                SortingAlg.tfqs = time.time()*1000
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


    def stoogesort(arr, l, h):
        if l >= h:
            return

        # If first element is smaller
        # than last,swap them
        if arr[l] > arr[h]:
            t = arr[l]
            arr[l] = arr[h]
            arr[h] = t

            if (h-l)<2:
                SortingAlg.nsts = SortingAlg.nsts + 1
                if SortingAlg.nsts % 10 == 0:
                    SortingAlg.tfsts = time.time()
                    print(arr)
                    print(SortingAlg.nsts)
                    SortingAlg.dicsts[SortingAlg.nsts] = SortingAlg.tfsts - SortingAlg.tists
                    SortingAlg.tists = SortingAlg.tfsts

        # If there are more than 2 elements in
        # the array
        if h - l + 1 > 2:
            t = (int)((h - l + 1) / 3)

            # Recursively sort first 2/3 elements
            SortingAlg.stoogesort(arr, l, (h - t))

            # Recursively sort last 2/3 elements
            SortingAlg.stoogesort(arr, l + t, (h))

            # Recursively sort first 2/3 elements
            # again to confirm
            SortingAlg.stoogesort(arr, l, (h - t))

    def reiniciarVar(self):
        SortingAlg.nis = 0
        SortingAlg.dicis = {}
        SortingAlg.tiis = 0
        SortingAlg.tfis = 0

        SortingAlg.nms = 0
        SortingAlg.dicms = {}
        SortingAlg.tims = 0
        SortingAlg.tfms = 0

        SortingAlg.nqs = 0
        SortingAlg.dicqs = {}
        SortingAlg.tiqs = 0
        SortingAlg.tfqs = 0

        SortingAlg.nsts = 0
        SortingAlg.dicsts = {}
        SortingAlg.tists = 0
        SortingAlg.tfsts = 0