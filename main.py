import logging
import sys
import heapsort
import numpy

def initLog():
    print("Initialize logging...")
    logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)

    fileName = u'log.txt'
    fileHandler = logging.FileHandler(fileName)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)
initLog()



def checkForSortedArray(aList):
    for i in range(len(aList)-1):
        if (aList[i] > aList[i+1]):
            logging.error("Array was not sorted: array[{0}]:{1} > array[{2}]:{3}".format(i, aList[i], i+1, aList[i+1]))
            return
    logging.info("*Checked for sorting*")

arrayToSort = numpy.random.randint(-100, 100, 10)
# arrayToSort = [-66, -37, -90, 70, -88]
# arrayToSort = [65, -55, 44, -44, 2, -84, 59, 77, 18, 78]
logging.info("Init array:\n{0}".format(arrayToSort))

heapSort = heapsort.HeapSort(arrayToSort)
logging.info("Heapsort sorted array:\n{0}".format(heapSort.sortedList))
checkForSortedArray(heapSort.sortedList)