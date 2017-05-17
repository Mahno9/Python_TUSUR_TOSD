from pprint import pprint, pformat
import logging
import sys
import numpy
import random

from heapsort import HeapSort
from quicksort import QuickSort
from graphs import Edge
from euler import Euler
from prim import Prim
from quicksort_search import QuickSortSearch

def initLog():
    print("Initialize logging...")
    logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)

    fileName = u'log.txt'
    fileHandler = logging.FileHandler(fileName, mode="w")
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)
initLog()

V = 100
needNonBoiled = 0.1*V
teapotV = 10

boiledV = 0
nonBoiledV = V
i = 0

# teapotPartOfV = teapotV / V
# while nonBoiledV >= needNonBoiled:
#     V_of_nonBoilded_for_boil = teapotPartOfV * nonBoiledV
#     V_of_boilded_for_boil = teapotPartOfV * boiledV
#     boiledV -= V_of_boilded_for_boil
#     nonBoiledV -= V_of_nonBoilded_for_boil
#
#     VForBoil = V_of_nonBoilded_for_boil + V_of_boilded_for_boil
#     boiledV += VForBoil
#     i+=1
#
#     logging.info("\n"
#                  "Шаг {0}\n"
#                  "Кипятилось кипячёной: {1}\n"
#                  "Кипятилось не кипячёной: {2}\n"
#                  "Кипячёной: {3}\n"
#                  "Не кипячёной: {4}\n".format(i, V_of_boilded_for_boil, V_of_nonBoilded_for_boil, boiledV, nonBoiledV))
#
# exit(0)  # Test for quarium task

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

arrSize = 10

arrayToSort = numpy.random.randint(-100, 100, arrSize)
logging.info("Init array:\n{0}\n".format(arrayToSort))

heapSort = HeapSort(arrayToSort)
logging.info("HeapSort sorted array:\n{0}".format(heapSort.sortedList))
checkForSortedArray(heapSort.sortedList)

quickSort = QuickSort(arrayToSort)
logging.info("QuickSort sorted array:\n{0}".format(quickSort.sortedList))
checkForSortedArray(quickSort.sortedList)

pos_to_search = random.randint(0, arrSize-1)
quickSort = QuickSortSearch(arrayToSort, pos_to_search)
logging.info("\n"
             "{2}\n"
             "Pos to search: {0}\nReturned value: {1}"
             .format(pos_to_search, quickSort.elem_val,
                     [[i, x] for i, x in enumerate(quickSort.sortedList)]))
checkForSortedArray(quickSort.sortedList)



graph = genereateGraph()
logging.info("Init graph:\n{0}\n".format(pformat(graph)))

primCalc = Prim(graph)
logging.info("Prim minimal spacing tree:\n{0}"
              .format(primCalc.minimalSpacingTree))

eulerCalc = Euler(graph)
eulerPathOrCycle = "cycle" if eulerCalc.eulerPath[0] == eulerCalc.eulerPath[-1]\
                    else "path"
logging.info("Euler {1}:\n{0}"
             .format(eulerCalc.eulerPath, eulerPathOrCycle))

