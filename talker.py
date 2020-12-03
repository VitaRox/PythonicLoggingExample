import logging
import time
import os
import string
import sys

from random import choices

"""
.. module:: talker_v1
:platform: Unix, Mac OSX
:synopsis: Console-input app demonstrating use of logs
.. moduleauthor:: Vita Harvey <vita.harvey@seattlecolleges.edu>
"""

# Configure logging

log_msg_format = "%(asctime)s (%(module)s --> %(funcName)s[%(lineno)d]) [%(levelname)s]: %(message)s"
# log_level = logging.DEBUG
# logging.basicConfig(filename=f"consoleapp{log_level}.log", filemode='w', format=log_msg_format, level=log_level)

# Create logging handler, formatting handler, file handler:
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(log_msg_format)

file_handler = logging.FileHandler('consoleapp.log')
file_handler.setFormatter(formatter)






"""
Counts the number of times the word, "imperdiet" appears in the given text

:param searchString: The name of the string to be analyzed for "imperdiet" occurrences
:type searchString: string
:returns: int - The number of times "imperdiet" appears in the text
"""
def countImperdiets(searchString):
    return searchString.count("imperdiet")


# Generates a log file containing log output
def generateLog():

    ## Counters

    # Init imperdietCount counter, the number of occurrences of "imperdiet" in this file.
    imperdietCount = 0
    # Init counter of number of sentences with "imperdiet".
    sentencesContainingImperdiet = 0
    # 'totalSentences' is the total number of sentences the user enters,
    # assuming user presses "enter" after entering each sentece.
    totalSentences = 0

    # Initialize fileMode in order to implement error-checking here:
    fileMode = ' '
    # Error handling for fileMode-selection input:
    while(fileMode != 'w' and fileMode != 'r'):
        # fileMode can be 'r' for 'read' or 'w' for 'write'
        fileMode = input("Please enter a 'w' for 'write mode' or a 'r' for 'read " +
            "  ")

    # Get name of file to read from or write to:
    ourFile = input("'write mode': Please enter the name of the file you wish to create.\n "
        + "'read mode' Please enter the name of the file to read from.\n")


    # Open the file to be read from/written to using the appropriate name and file-mode.

    # If user enters 'w' for 'write', append a '+' to 'fileMode' so
    # can be written to AND read from(for counting purposes).
    if(fileMode == 'w'):
        fileMode = "w+"
    # "openFile" is object representing the file we're reading from/writing to.
    openFile = open(ourFile + ".txt", fileMode)

    # Conditionally handle user input depending on fileMode user entered.
    # 'Write' mode:
    # Prime 'userIn' variable: serves as flag to exit input mode as well as collecting
    # user input itself.
    userIn = ''
    if(fileMode == 'w+'):
        while(userIn != 'X'):
            userIn = (input("Please type a sentence and press 'enter', or enter 'X' to quit, save, and exit: "))
            if("imperdiet" in userIn):
                # Increment our imperdiet-sentences counter:
                sentencesContainingImperdiet = sentencesContainingImperdiet + 1
                # Update our imperdietCount with the number of "imperdiet" occurrences on this line:
                imperdietCount += countImperdiets(userIn)
            totalSentences = totalSentences + 1
            openFile.write(userIn + '\n')
        print("User entered " + str(totalSentences - 1) + " sentences.\n")
        openFile.close()

    # 'Read' mode:
    elif(fileMode == 'r'):
        # Create string/object "readFile" associated with contents of "ourFile", the file to be read from:
        dividedLines = openFile.readlines()

        # Analyze readFile:
        # Split string representing file's text contents into sentences.

        totalSentences = len(dividedLines)
        # Iterate through list representing text of document.
        for line in dividedLines:
            # Update total number of "imperdiet" in document:
            imperdietCount += line.count("imperdiet")
            # Update number of lines containing "imperdiet" if current sentence contains it.
            if("imperdiet" in line):
                sentencesContainingImperdiet = sentencesContainingImperdiet + 1



    ## Display final stats of log, output 'consoleapp.log' file.
    print("Found " + str(imperdietCount) + " occurrences of the word 'imperdiet'.\n")
    print("There were " + str(sentencesContainingImperdiet) + " sentences containing 'imperdiet'.\n")


# Main application method
def main():
    # call our console input function
    generateLog()

# Execute this program by calling main()
main()
