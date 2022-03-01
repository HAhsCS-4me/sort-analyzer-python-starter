# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
# print(randomData[0:50])
# print(reversedData[0:50])
# print(nearlySortedData[0:50])
# print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")


# Bubble Sort Function
def bubbleSort(anArray):
	for numComparison in range(len(anArray) - 1, 0 , -1):
		for i in range(numComparison):
			if anArray[i] > anArray[i + 1]:
				anArray[i], anArray[i + 1] = anArray[i + 1], anArray[i]

# Selection Sort Function
def selectionSort(anArray):
    for i in range(len(anArray) - 2):
        minPosition = i
        for j in range(i + 1, len(anArray)):
            if anArray[j] < anArray[minPosition]:
                minPosition = j 
        anArray[minPosition], anArray[i] = anArray[i], anArray[minPosition]

# Insertion Sort Function
def insertionSort(anArray):
    for i in range(1, len(anArray)):
        insertVal = anArray[i] 
        insertPos = i
        while insertPos >= 1 and anArray[insertPos - 1] > insertVal: 
            anArray[insertPos] = anArray[insertPos - 1]
            insertPos -= 1
        anArray[insertPos] = insertVal


# Output for Bubble, Selection, Insertion Sort for Random Data
startTime = time.time()
selectionSort(randomData)
endTime = time.time()
print(f"Sort Random Data: {endTime - startTime} seconds")

# Output for Bubble, Selection, Insertion Sort for Reversed Data
'''startTime = time.time()
selectionSort(reversedData)
endTime = time.time()
print(f"Sort Reversed Data: {endTime - startTime} seconds")'''

# Output for Bubble, Selection, Insertion Sort for Nearly Sorted Data
'''startTime = time.time()
selectionSort(nearlySortedData)
endTime = time.time()
print(f"Sort Nearly Sorted Data: {endTime - startTime} seconds")'''

# Output for Bubble, Selection, Insertion Sort for Few Unique Data
'''startTime = time.time()
selectionSort(fewUniqueData)
endTime = time.time()
print(f"Sort Few Unique Data: {endTime - startTime} seconds")'''