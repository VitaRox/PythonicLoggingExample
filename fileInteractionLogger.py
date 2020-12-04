import logging
import logging.config

import time

import sys

"""
.. module:: main.py_v1
:platform: Unix, Windows
:synopsis: Console-input app demonstrating use of logs
.. moduleauthor:: Vita Harvey <vita.harvey@seattlecolleges.edu>
"""

# Configure logging
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# Create logger instance
logger = logging.getLogger(__name__)

"""
Counts the number of times the word, "imperdiet" appears in the given text

:param searchString: The name of the string to be analyzed for "imperdiet" occurrences
:type searchString: string
:returns: int - The number of times "imperdiet" appears in the text
"""
def countImperdiets(searchString):
    logger.debug("Using countImperdiets() to count occurences")
    return searchString.count("imperdiet")


# Generates a log file containing log output
def useConsole():

    logger.debug("useConsole() called")

    ## Counters

    # Init imperdietCount counter, the number of occurrences of "imperdiet" in this file.
    logger.debug("# Init imperdietCount counter, the number of occurrences of 'imperdiet' in this file")
    imperdietCount = 0

    # Init counter of number of sentences with "imperdiet".
    logger.debug("# Init counter of number of sentences with 'imperdiet'")
    sentencesContainingImperdiet = 0

    # 'totalSentences' is the total number of sentences the user enters or is read from input file
    logger.debug("# Init 'totalSentences', the total number of sentences the user enters or is read from input file")
    totalSentences = 0

    ## Flags

    # Initialize fileMode
    logger.info("Getting user input:")
    logger.debug("# Init fileMode")
    fileMode = ''

    # userError is a flag that allows for us to init fileMode to '' without unnecessary log output
    logger.debug("userError = 0, tracking # of mistaken user inputs:")
    userError = 0
    # Error handling for fileMode-selection input:
    while(fileMode != 'w' and fileMode != 'r'):
        # fileMode can be 'r' for 'read' or 'w' for 'write'
        fileMode = input("Please enter a 'w' for 'write mode' or a 'r' for 'read " +
            "  ")

        # userError and following code is for retrospective analytics, re:UX:
        # tldr: Determine if this interface is usable by most end-users in
        # most use-cases.
        logger.debug("Incremement userError by 1")
        userError += 1
        if(userError > 0 and fileMode != 'r' and fileMode != 'w'):
            logger.error("user has made " + str(userError) + " errors attempting to enter the fileMode.")

    # Get name of file to read from or file to write to:
    ourFile = input("'write mode': Please enter the name of the file you wish to create.\n "
        + "'read mode' Please enter the name of the file to read from.\n")

    # Open the file to be read from/written to using the appropriate name and file-mode
    logger.debug("User opened " + ourFile + " with the "  + "'" + fileMode + "'"+ " file-mode.")

    # If user enters 'w' for 'write', append a '+' to 'fileMode' so
    # can be written to AND read from (for counting purposes)
    if(fileMode == 'w'):
        fileMode = "w+"
    # 'openFile' is object representing the file we're reading from/writing to
    openFile = open(ourFile + ".txt", fileMode)
    logger.debug(ourFile + " is object representing the file we're reading from/writing to")

    # Conditionally handle user input depending on fileMode user entered
    logger.debug("# Conditionally handle user input depending on fileMode user entered.")

    # 'WRITE' mode:
    logger.debug("'Write' mode: writing to " + ourFile)
    # Prime 'userIn' variable: serves as flag to exit input mode as well as collecting
    # user input itself.
    logger.debug("Prime userIn: userIn = ''")
    userIn = ''
    if (fileMode == 'w+'):
        while(userIn != 'X'):
            userIn = (input("Please type a sentence and press 'enter', or enter 'X' to quit, save, and exit: "))
            if ("imperdiet" in userIn):
                # Increment our imperdiet-sentences counter:
                sentencesContainingImperdiet = sentencesContainingImperdiet + 1
                # Update our imperdietCount with the number of "imperdiet" occurrences on this line:
                imperdietCount += countImperdiets(userIn)
            totalSentences = totalSentences + 1
            openFile.write(userIn + '\n')
        logger.debug("User entered " + str(totalSentences - 1) + " sentences.\n")
        print("User entered " + str(totalSentences - 1) + " sentences.\n")
        openFile.close()

    # 'READ' mode:
    elif (fileMode == 'r'):
        logger.info("'Read' mode: reading from " + ourFile)
        # Create string/object "readFile" associated with contents of "ourFile", the file to be read from:
        readFile = openFile.readlines()

        # Analyze readFile
        logger.info("Analyzing " + ourFile)

        # Split string representing file's text contents into sentences
        totalSentences = len(readFile)
        logger.debug("totalSentences = " + str(totalSentences))

        # Iterate through list representing text of document
        logger.debug("Set number of lines to 0; will be used to enumberate the lines of our input file")
        lines = 0
        for line in readFile:
            lines += 1
            logger.debug("For line " + str(lines) + " in readFile: ")
            # Update total number of "imperdiet" in document:
            imperdietCount += line.count("imperdiet")
            logger.debug(str(imperdietCount) + " instances of 'imperdiet' thus far.")
            # Update number of lines containing "imperdiet" if current sentence contains it
            if("imperdiet" in line):
                logger.debug("'Imperdiet' in this line?: " + str("imperdiet" in line))
                sentencesContainingImperdiet = sentencesContainingImperdiet + 1

    # Display final stats of log, output 'consoleapp.log' file
    logger.debug("# Display final stats of log, output 'consoleapp.log' file")

    print("Found " + str(imperdietCount) + " occurrences of the word 'imperdiet'.\n")
    logger.debug("Found " + str(imperdietCount) + " occurrences of the word 'imperdiet'.\n")

    print("There were " + str(sentencesContainingImperdiet) + " sentences containing 'imperdiet'.\n")
    logger.debug("There were " + str(sentencesContainingImperdiet) + " sentences containing 'imperdiet'.\n")


# Main application method
def main():
    logger.info("Calling application method now")

    startTime = time.time()
    logger.info("Start execution time: " + str(startTime))

    # call our console input function
    logger.info("Call useConsole() method: ")
    useConsole()

    endTime = time.time()
    logger.info("End execution time = " + str(endTime))

    totalRuntime = endTime - startTime
    logger.info("Total runtime: " + str(totalRuntime))

# Execute this program by calling the application method
main()
