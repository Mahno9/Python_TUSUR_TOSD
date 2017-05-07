import logging
import swap


class QuickSort:
    inputList = []
    sortedList = []

    def __init__(self, inputList):
        try:
            self.inputList = list(inputList)
            self.sortedList = list(self.inputList)
            self.quicksort(self.sortedList)
        except BaseException:
            logging.error("Error occurred while sort array:")


    def quicksort(self, aList, beginPos = None, endPos = None):
        if beginPos is None or endPos is None:
            beginPos = 0
            endPos = len(aList)-1

        pivot = aList[(beginPos+endPos)//2]
        l = beginPos
        r = endPos

        while l <= r:
            while aList[l] < pivot:
                l += 1
            while aList[r] > pivot:
                r -= 1
            if l <= r:
                swap.swap(aList, l, r)
                l += 1
                r -= 1

        if beginPos < r:
            self.quicksort(aList, beginPos, r)
        if endPos > l:
            self.quicksort(aList, l, endPos)
