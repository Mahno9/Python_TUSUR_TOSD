import logging
import swap


class QuickSortSearch:
    inputList = []
    sortedList = []
    elem_val = None

    def __init__(self, inputList, elem_pos):
        try:
            self.inputList = list(inputList)
            self.sortedList = list(self.inputList)
            self.elem_val = self.quicksort_search(self.sortedList, elem_pos)
        except BaseException:
            logging.error("Error occurred while sort array:")

    def quicksort_search(self, aList, elem_pos, beginPos=None, endPos=None):
        if elem_pos is None:
            return None
        if beginPos is None or endPos is None:
            beginPos = 0
            endPos = len(aList) - 1

        if beginPos == endPos and beginPos == elem_pos:
            return aList[beginPos]

        pivot = aList[(beginPos + endPos) // 2]
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

        retVal = None
        if beginPos <= r and elem_pos <= r:
            retVal = self.quicksort_search(aList, elem_pos, beginPos, r)
        if retVal is None and endPos >= l and elem_pos >= l:
            retVal = self.quicksort_search(aList, elem_pos, l, endPos)

        if retVal is None:
            return pivot
        else:
            return retVal
