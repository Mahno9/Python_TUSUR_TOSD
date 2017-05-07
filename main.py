from pprint import pprint, pformat
import logging
import sys
import numpy

from heapsort import HeapSort
from quicksort import QuickSort
from prim import Prim
from graphs import Edge

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
    for i in range(len(aList) - 1):
        if (aList[i] > aList[i + 1]):
            logging.error(
                "Array was not sorted: array[{0}]:{1} > array[{2}]:{3}".format(i, aList[i], i + 1, aList[i + 1]))
            return
    logging.info("*Checked for sorting*\n")


def genereateGraph():
    graph = [
        Edge("A", "B", 7),
        Edge("A", "D", 5),
        Edge("C", "B", 8),
        Edge("D", "B", 9),
        Edge("E", "B", 7),
        Edge("D", "E", 15),
        Edge("C", "E", 5),
        Edge("F", "E", 8),
        Edge("G", "E", 9),
        Edge("D", "F", 6),
        Edge("G", "F", 11)
    ]
    return graph


arrayToSort = numpy.random.randint(-100, 100, 10)
logging.info("Init array:\n{0}\n".format(arrayToSort))

heapSort = HeapSort(arrayToSort)
logging.info("HeapSort sorted array:\n{0}".format(heapSort.sortedList))
checkForSortedArray(heapSort.sortedList)

quickSort = QuickSort(arrayToSort)
logging.info("QuickSort sorted array:\n{0}".format(quickSort.sortedList))
checkForSortedArray(quickSort.sortedList)


graph = genereateGraph()
logging.info("Init graph:\n{0}\n".format(pformat(graph)))

primCalc = Prim(graph)
logging.info("Prim minimal spacing tree:\n{0}".format(primCalc.minimalSpacingTree))

