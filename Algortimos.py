import time
import math

class SortingAlg:
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
        print(A)
        n=0;
        dict={}
        milis = time.time()
        for j in range (0,len(A)):
            n=n+1
            if(n%10==0):
                milis2=time.time()
                dict[n]=milis2-milis
            key=A[j]
            i=j-1
            while i>(-1) and A[i]>key:
                A[i+1]=A[i]
                i=i-1
            A[i+1]=key
        print(A)
        return dict

    def mergeSort(alist):
        if SortingAlg.nms==0:
            SortingAlg.tims=time.time()
        print("Splitting ", alist)
        if len(alist)==1:
            SortingAlg.nms=SortingAlg.nms+1
            if SortingAlg.nms % 10 == 0:
                SortingAlg.tfms=time.time()
                print(SortingAlg.nms)
                SortingAlg.dicms[SortingAlg.nms]=SortingAlg.tfms-SortingAlg.tims
        if(SortingAlg.nms==100):
            print(SortingAlg.dicms)
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
        print("Merging ", alist)

    def quicksort(alist):
        SortingAlg.tiqs = time.time()
        SortingAlg.quickSortHelper(alist,0,len(alist)-1)

    def quickSortHelper(alist,first,last):

        if(first==last):
            SortingAlg.nqs = SortingAlg.nqs + 1
            if SortingAlg.nqs % 10 == 0:
                SortingAlg.tfqs = time.time()
                print(SortingAlg.nqs)
                SortingAlg.dicqs[SortingAlg.nqs] = SortingAlg.tfqs - SortingAlg.tiqs

        if first<last:
            splitpoint = SortingAlg.partition(alist,first,last)
            SortingAlg.nqs = SortingAlg.nqs + 1
            if SortingAlg.nqs % 10 == 0:
                SortingAlg.tfqs = time.time()
                print(SortingAlg.nqs)
                SortingAlg.dicqs[SortingAlg.nqs] = SortingAlg.tfqs - SortingAlg.tiqs
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
