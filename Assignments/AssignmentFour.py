"""
   Author : Kyle Drnovscek
   Revison date : 17 December 2024
   Program : Reading Files and Searching for Data
   Description : A program Searches wordle file data based on your input
   VARIABLE DICTIONARY :
   filename : (string) The name of the file containing Wordle data.
   fileHandler : (file) File object for reading the Wordle data file.
   dataLines : (list) List of strings, each representing a line in the Wordle data file.
   words : (list) List of Wordle words from the file.
   dates : (list) List of corresponding dates for the Wordle words.
   original_dates : (list) Copy of the dates list to maintain original order.
   original_words : (list) Copy of the words list to maintain original order.
   earliestDate : (int) The earliest date in the dataset, in merged integer format.
   latestDate : (int) The latest date in the dataset, in merged integer format.
   valid : (bool) Flag to check if user input is valid.
   userOption : (string) Stores the user choice for word or date search.
   userInput : (string) The word entered by the user during a search.
   year : (string) Year input by the user for a date search.
   month : (string) Month input by the user for a date search.
   day : (string) Day input by the user for a date search.
   mergedDate : (int) A date represented as a merged integer (YYYYMMDD).
   line_int : (string) Temporary string for building merged date.
   leftWords, (rightWords) list : Temporary arrays for merge sort, containing word segments.
   leftDates, (rightDates) list : Temporary arrays for merge sort, containing date segments.
   i, j, k : (int) Indices for iterating through lists during merge sort.

"""

# Function to perform merge sort on the word and date lists
def mergeSort(wordList, dateList, leftIndex, rightIndex):
    if leftIndex < rightIndex:
        # Find the middle index to divide the array
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2
        
        # Recursively sort the left and right halves
        mergeSort(wordList, dateList, leftIndex, middleIndex)
        mergeSort(wordList, dateList, middleIndex + 1, rightIndex)
        
        # Merge the sorted halves
        mergeSortMerge(wordList, dateList, leftIndex, middleIndex, rightIndex)

# Helper function to merge two sorted halves
def mergeSortMerge(wordList, dateList, leftIndex, middleIndex, rightIndex):
    # Calculate sizes of temporary arrays
    n1 = middleIndex - leftIndex + 1
    n2 = rightIndex - middleIndex

    # Create temporary arrays for words and dates
    leftWords = [0] * n1
    rightWords = [0] * n2
    leftDates = [0] * n1
    rightDates = [0] * n2

    # Copy data into temporary arrays
    for i in range(n1):
        leftWords[i] = wordList[leftIndex + i]
        leftDates[i] = dateList[leftIndex + i]
    for j in range(n2):
        rightWords[j] = wordList[middleIndex + 1 + j]
        rightDates[j] = dateList[middleIndex + 1 + j]

    # Merge the temporary arrays back into the original list
    i, j, k = 0, 0, leftIndex
    while i < n1 and j < n2:
        if leftWords[i] <= rightWords[j]:
            wordList[k] = leftWords[i]
            dateList[k] = leftDates[i]
            i += 1
        else:
            wordList[k] = rightWords[j]
            dateList[k] = rightDates[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left array
    while i < n1:
        wordList[k] = leftWords[i]
        dateList[k] = leftDates[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right array
    while j < n2:
        wordList[k] = rightWords[j]
        dateList[k] = rightDates[j]
        j += 1
        k += 1 

# Function to merge date components into a single integer
def merge(year, month, day):
    try:
        months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        line_int = ""
        line_int += year
        month_str = str(months.index(month.lower()) + 1)
        if len(month_str) == 1:
            month_str = "0" + month_str
        line_int += month_str
        line_int += day
        return int(line_int)
    except:
        return 0

# Function to check if a word exists and return its corresponding date
def isMatch(A, wordList, dateList):
    index = binarySearch(wordList, A)
    if index != -1:
        return dateList[index]
    return 0

# Binary search function to find the index of a value in a sorted array
def binarySearch(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# Open the file containing Wordle data
filename = "wordle.dat"
fileHandler = open(filename, "r")

# Read all lines from the file
dataLines = fileHandler.readlines()
for i in range(len(dataLines)):
    dataLines[i] = dataLines[i].strip()

# Initialize lists to store words and dates
words = []
dates = []
for line in dataLines:
    # Split each line into components
    month, day, year, word = line.split()
    # Merge date components into a single date
    mergedDate = merge(year, month, day)
    # Append the date to the dates list
    dates.append(mergedDate)
    # Append the word to the words list
    words.append(word)

# Get the start and end dates from the dates list
earliestDate = dates[0]
latestDate = dates[len(dates) - 1]

# Create a copy of dates to maintain the original order
original_dates = dates.copy()
original_words = words.copy()

# Sort the words and dates using merge sort
mergeSort(words, dates, 0, len(words) - 1)

print("Welcome to the Wordle Database!")
valid = False
userOption = ""
while not valid:
    # Prompt the user to choose an option
    userOption = input("Enter w if you are looking for a word, or d for a word on a certain date: ")
    if userOption.lower() == "w":
        valid = True
    elif userOption.lower() == "d":
        valid = True

if userOption == "w":
    valid = False
    while not valid:
        # Prompt the user to enter a word
        userInput = input("What word are you looking for? ").upper()
        if len(userInput) == 5:
            valid = True
    # Check if the word matches any in the database
    date = isMatch(userInput, words, dates)
    if date:
        print("The word %s was the solution to the puzzle on %d." % (userInput, date))
    else:
        print("%s was not found in the database." % userInput)
elif userOption == "d":
    valid = False
    while not valid:
        # Prompt the user to enter a date
        year = input("Enter the year: ")
        month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
        day = input("Enter the day: ")
        # Pad single-digit days with a leading zero
        if len(day) == 1:
            day = "0" + day
        # Merge date components into a single date
        date = merge(year, month, day)
        if date != 0:
            valid = True
    word = isMatch(date, original_dates, original_words)
    if date < earliestDate:
        print("%d is too early. No wordles occurred before %d. Enter a later date." % (date, earliestDate))
    elif date > latestDate:
        print("%d is too recent. Our records only go as late as %d. Please enter an earlier date." % (date, latestDate))
    if word:
        print("The word entered on %d was %s." % (date, word))

