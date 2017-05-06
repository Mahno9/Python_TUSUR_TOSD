import logging

class HeapSort:
    inputList = []
    sortedList = []

    def __init__(self, inputList):
        try:
            self.inputList = list(inputList)
            self.sortedList = list(self.inputList)
            self.heapsort(self.sortedList)
        except BaseException:
            logging.error("Error occurred while sort array:")


    def heapsort(self, aList):
        # convert aList to heap
        lastPos = len(aList) - 1
        lastParent = lastPos // 2
        for i in range(lastParent, -1, -1):
            self.moveDown(aList, i, lastPos)

        # flatten heap into sorted array
        for i in range(lastPos, 0, -1):
            if aList[0] > aList[i]:
                self.swap(aList, 0, i)
                self.moveDown(aList, 0, i - 1)


    def moveDown(self, aList, parentPos, lastPos):
        largestPos = 2 * parentPos + 1
        while largestPos < lastPos:
            # right child exists and is larger than left child
            if (largestPos < lastPos) and (aList[largestPos] < aList[largestPos + 1]):
                largestPos += 1

            # largest child is larger than parent
            if aList[largestPos] > aList[parentPos]:
                self.swap(aList, largestPos, parentPos)
                # move down to largest child
                parentPos = largestPos
                largestPos = 2 * parentPos + 1
            else:
                return  # force exit


    def swap(self, A, x, y):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp