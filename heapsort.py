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
        for lastPos in range(len(aList) - 1, 0, -1):
            lastParent = (lastPos - 1) // 2
            for i in range(lastParent, -1, -1):
                self.moveDown(aList, i, lastPos)
            if aList[0] > aList[lastPos]:
                self.swap(aList, 0, lastPos)

    def moveDown(self, aList, parentPos, lastPos):
        largestPos = 2 * parentPos
        if aList[largestPos + 1] > aList[largestPos]:
            largestPos += 1
        if aList[largestPos] > aList[parentPos]:
            self.swap(aList, largestPos, parentPos)

    def swap(self, A, x, y):
        A[x], A[y] = A[y], A[x]
