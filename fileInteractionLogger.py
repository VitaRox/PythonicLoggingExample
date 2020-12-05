import logging
import logging.config
import time
import os.path

"""
.. module:: fileInteractionLogger_v1
:platform: Unix, Windows
:synopsis: Console-input app demonstrating use of logs
.. moduleauthor:: Vita Harvey <vita.harvey@seattlecolleges.edu>
"""
# Configure logging
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# Create logger instance
logger = logging.getLogger(__name__)

# A simple function to dynamically change the desired log level of the log output
def resetLogLevel():
    logger.info("Simple function to dynamically change the desired log level of the log output")
    logLevel = input("Please enter the desired log level. Default is DEBUG: ")
    while (logLevel.lower() not in ("debug", "info", "warning", "error", "critical")):
        logLevel = input("Please enter the desired log level. Default is DEBUG: ")
    logger.setLevel(logLevel.upper())
    for handler in logger.handlers:
        handler.setLevel(logLevel.upper())

"""
Counts the number of times the word, "imperdiet" appears in the given text

:param searchString: The name of the string to be analyzed for "imperdiet" occurrences
:type searchString: string
:returns: int - The number of times "imperdiet" appears in the text
"""
def countImperdiets(searchString):
    logger.debug("Using countImperdiets() to count occurrences")
    return searchString.count("imperdiet")

"""
Returns a rounded version of the time elapsed between the given times

:param endTime: Final recorded time
:type endTime: float
:param startTime: Begin recorded time
:type startTime: float
:returns: float - The delta between the given endTime and startTime
"""
def getElapsedTime(endTime, startTime):
    logger.debug("getElapsedTime() called")
    return round(endTime - startTime, 4)

"""
Calculates the average time to read or write a line

:param elapsedTime: How much time has passed between start and stop of process
:type elapsedTime: float
:param totalLines: Total number of sentences/lines being examined
:type int
:returns: float - The average time to read or write each line
"""
def getAverageTimePerLine(elapsedTime, totalLines):
    return elapsedTime / totalLines

##
#  Gets user input via console, uses to either read from or write to a given file,
#  analyzes file contents, program performance, user actions, and generates a log file
#  called "consoleapp.log"
def useConsole():

    logger.debug("useConsole() called")

    # Allow user to customize level of logging output
    customizedRootLogLevel = 'n'
    customizedRootLogLevel = input("Customize root log level? Default is DEBUG/TRACE. Enter 'n' for no or 'y' for yes:")
    if (customizedRootLogLevel.lower() == 'y'):
        logger.info("Calling resetLogLevel() now.")
        resetLogLevel()
    while (customizedRootLogLevel.lower() != 'y' and customizedRootLogLevel.lower() != 'n'):
        customizedRootLogLevel = input("Customize root log level? Default is DEBUG/TRACE. Enter 'n' for no or 'y' for yes:")

    ## Counters
    logger.info("INIT COUNTERS")

    # Init imperdietCount counter, the number of occurrences of "imperdiet" in this file.
    logger.info("# Init imperdietCount counter, the number of occurrences of 'imperdiet' in this file.")
    imperdietCount = 0
    logger.debug("imperdietCount initialized to = " + str(imperdietCount))

    # Init counter of number of sentences/lines with "imperdiet".
    logger.info("# Init counter of number of sentences/lines with 'imperdiet'")
    sentencesContainingImperdiet = 0
    logger.debug("sentencesContainingImperdiet initialized to = " + str(sentencesContainingImperdiet))

    # 'totalLines' is the total number of sentences/lines the user enters or is read from input file
    logger.info("# Init 'totalLines', the total number of sentences/lines the user enters or is read from input file")
    totalLines = 0
    logger.debug("totalLines initialized to = " + str(totalLines))

    # Init imperdietSearchTime, the total amount of time spent looking for instances of "imperdiet"
    logger.info("# Init imperdietSearchTime, total amt of time spent looking for 'imperdiet' in file")
    imperdietSearchTime = 0
    logger.debug("imperdietSearchTime initialized to = " + str(imperdietSearchTime))

    ## Flags
    logger.info("INIT FLAGS")

    # Initialize fileMode
    logger.info("# Init fileMode")
    fileMode = ''
    logger.debug("fileMode initialized to = " + fileMode)

    logger.info("Getting user input: ")

    # userError is a flag that allows for us to init fileMode to '' without unnecessary log output
    logger.info("userError tracks # of mistaken user inputs")
    userError = 0
    logger.debug("userError initialized to = " + str(userError))
    # Error handling for fileMode-selection input:
    while (fileMode != 'w' and fileMode != 'r'):
        # fileMode can be 'r' for 'read' or 'w' for 'write'
        fileMode = input("Please enter a 'w' for 'write mode' or a 'r' for 'read " +
            "  ")
        # userError and following code is for retrospective analytics, re:UX:
        # tldr: Use to determine if this interface is usable by most end-users in
        # most use-cases.
        logger.debug("Incremement userError by 1")
        userError += 1
        if (userError > 0 and fileMode != 'r' and fileMode != 'w'):
            logger.warning("user has made " + str(userError) + " errors attempting to enter the fileMode.")

    # Get name of file to read from or file to write to:
    ourFile = input("'write mode': Please enter the name of the file you wish to create.\n "
        + "'read mode' Please enter the name of the file to read from.\n")
    logger.info("User entered the file-name " + ourFile)

    # Conditionally handle user input depending on fileMode user entered
    logger.info("# Conditionally handle user input depending on fileMode user entered.")

    # Open the file to be read from/written to using the appropriate name and file-mode
    logger.debug("User opened " + ourFile + " in the "  + "'" + fileMode + "'" + " file-mode.")

    # If user enters 'w' for 'write', append a '+' to 'fileMode' so
    # can be written to AND read from (for counting purposes)
    if (fileMode == 'w'):

        fileMode = "w+"
        logger.debug("'w' converted to 'w+': fileMode = " + fileMode)
        # Check to make sure file doesn't already exist/get overwritten:
        logger.info("# Check to make sure file doesn't already exist/get overwritten:")

        while os.path.isfile(ourFile + ".txt"):
            logger.warning("File by that name in this namespace already exists! Proceeding will override the existing file.")
            # Re-prompt user for file name:
            ourFile = input("'write mode': Please enter the name of the file you wish to create.\n "
                + "'read mode' Please enter the name of the file to read from.\n")
            logger.info("User entered the file-name " + ourFile)
    try:
        # 'openFile' is object representing the file we're reading from/writing to
        # 'ourFile' is a string representing name of 'openFile'
        openFile = open(ourFile + ".txt", fileMode)
        logger.debug(ourFile + " is the object representing the file we're reading from/writing to")
    except IOError as ioe:
        logger.exception("Error creating file to write to: " + str(ioe))

    # Init performanceStats tuple
    logger.info("# Init performanceStats tuple")
    performanceStats = ("", "", "")

    ####
    ## 'WRITE' mode:
    ####
    logger.debug("'WRITE' mode: writing to " + ourFile + ".txt")
    # Init 'userIn' variable:
    # Serves as flag to exit input mode, as well as collecting user input itself.
    logger.info("# Serves as flag to exit input mode, as well as collecting user input itself.")
    userIn = ''
    logger.debug("Init userIn variable to ''; userIn = " + userIn)

    if (fileMode == 'w+'):

        # subtotalTime is a counter to track the total time spent entering sentences
        logger.info("# subtotalTime is a counter to track the total time spent entering sentences")
        subtotalTime = 0
        logger.debug("Init subtotalTime counter to = " + str(subtotalTime) + " seconds")

        # Prime initial startWriteTime value to begin writing first line
        logger.info("# Prime initial startWriteTime value to begin writing first line")
        startWriteTime = time.time()
        startImperdietTime = startWriteTime
        logger.info("initial startImperdietTime = " + str(round(startImperdietTime, 4)))
        logger.info("initial startWriteTime = " + str(round(startWriteTime, 4)))

        while (userIn.lower() != 'x'):

            logger.info("Awaiting user input (userIn) via console")
            userIn = (input("Please type a sentence and press 'enter', or enter 'x' to quit, save, and exit: "))
            logger.debug("userIn is now = " + userIn)

            if ("imperdiet" in userIn):

                endImperdietTime = time.time()
                logger.info("endImperdietTime = " + str(round(endImperdietTime, 4)))

                elapsedImperdietTime = getElapsedTime(endImperdietTime, startImperdietTime)
                logger.info("elapsedImperdietTime = " + str(round(elapsedImperdietTime, 4)))

                # Update the imperdietSearchTime
                imperdietSearchTime += elapsedImperdietTime
                logger.debug("imperdietSearchTime is now totalling " + str(imperdietSearchTime) + " seconds.")

                # Increment our imperdiet-sentences counter, sentencesContainingImperdiet:
                logger.info("# Increment our imperdiet-sentences counter, sentencesContainingImperdiet: ")
                sentencesContainingImperdiet += 1
                logger.debug("sentencesContainingImperdiet is now = " + str(sentencesContainingImperdiet))

                # Update our imperdietCount with the number of 'imperdiet' occurrences on this line:
                logger.info("# Update our imperdietCount with the number of 'imperdiet' occurrences on this line:")
                imperdietCount += countImperdiets(userIn)
                logger.debug("imperdietCount is now " + str(imperdietCount))

            # Increment totalLines:
            logger.info("# Increment totalLines: ")
            totalLines += 1
            logger.debug("totalLines is now " + str(totalLines) + " lines.")

            try:
                logger.debug("Writing line #" + str((totalLines - 1)) + " to output .txt file...")
                openFile.write(userIn + '\n')

                # Mark the endTime of writing the line
                endWriteTime = time.time()
                logger.info("# Mark the endTime of writing the line: " + str(round(endWriteTime, 4)))
                subtotalTime += getElapsedTime(endWriteTime, startWriteTime)
                logger.debug("subtotalTime now = " + str(subtotalTime))

                # Begin startTime for next line
                logger.info("# Mark the startTime of writing the next line: " + str(round(startWriteTime, 4)))
                startWriteTime = time.time()
            except IOError as ioe:
                logger.exception("Error occurred writing line to file: " + str(ioe))

        logger.debug("Exit user input WRITE loop")

        # Compensate for fencepost scenario in above 'for' loop: totalLines--
        totalLines -= 1
        logger.info("User entered " + str(totalLines) + " sentences.")
        averageTimeToWriteLine = getAverageTimePerLine(subtotalTime, totalLines)
        logger.info("Average time to enter a sentence: " + str(round(averageTimeToWriteLine, 4)) + " seconds.")

        # Calculate average time to find "imperdiet" in a sentence
        logger.info("# Calculate average time to find 'imperdiet' in a sentence: getAverageTime(imperdietSearchTime / totalLines)")
        averageImperdietSearchTime = getAverageTimePerLine(imperdietSearchTime, totalLines)
        logger.debug("Average time to find 'imperdiet' in a sentence: " + str(round(averageImperdietSearchTime, 4)) + " seconds.")
        performanceStats = (averageImperdietSearchTime, )
        print("\nUser entered " + str(totalLines) + " sentences.\n")

        # performanceStats = (averageTimeToReadOrWriteLine, averageTimeToFindImperdiet, fileMode)
        # Update tuple containing the performance stats
        logger.info("# performanceStats = (averageTimeToReadOrWriteLine, averageTimeToFindImperdiet, fileMode)")
        performanceStats = (averageTimeToWriteLine, averageImperdietSearchTime, fileMode)
    ## END WRITE OPERATION

    ####
    ## 'READ' mode:
    ####
    elif (fileMode == 'r'):

        # Prime initial startReadTime value to begin reading first line
        logger.info("# Get initial startReadTime value to begin reading first line")
        startReadTime = time.time()
        logger.info("Initial startReadTime = " + str(round(startReadTime, 4)))
        logger.debug("'READ' mode: reading from " + ourFile + ".txt")

        try:
            # Create string/object "readFile" associated with contents of "ourFile", the file to be read from:
            readFile = openFile.readlines()
            logger.debug("Successfully opening/reading readFile")
        except EOFError as eofe:
            logger.exception("Error occurred attempting to read from input file: " + str(eofe))

        # Analyze readFile
        logger.info("Analyzing " + ourFile + ".txt")

        # Split string representing file's text contents into lines
        logger.info("# Split string representing file's text contents into lines")
        totalLines = len(readFile)
        logger.debug("totalLines = " + str(totalLines))

        # Iterate through list representing text of document
        logger.info("Set number of lines to 0; will be used to enumerate the lines of our input file")
        lines = 0
        logger.debug("lines = " + str(lines))
        logger.debug("for line in readFile")

        for line in readFile:

            startImperdietReadTime = time.time()
            logger.info("In line #" + str(line) + ", startImperdietReadTime = " + str(round(startImperdietReadTime, 4)))
            lines += 1
            logger.debug("For line " + str(lines) + " in readFile: ")

            # Update total number of 'imperdiet' found in document:
            logger.info("# Update total number of 'imperdiet' found in document:")
            imperdietCount += line.count("imperdiet")
            logger.debug(str(imperdietCount) + " instances of 'imperdiet' thus far.")
            logger.debug("'Imperdiet' in this line = " + str("imperdiet" in line))

            if ("imperdiet" in line):

                endImperdietReadTime = time.time()
                imperdietSearchTime += getElapsedTime(endImperdietReadTime, startImperdietReadTime)
                logger.debug("imperdietSearchTime is now " + str(round(imperdietSearchTime, 4)) + " seconds.")

                # Update number of lines containing "imperdiet" if current sentence contains it
                logger.info("# Update number of lines containing 'imperdiet' if current sentence contains it")
                sentencesContainingImperdiet += 1
                logger.debug("sentencesContainingImperdiet now = " + str(sentencesContainingImperdiet))

        logger.info("# When finished reading file, get endReadTime")
        # When finished reading file, get endReadTime of file
        endReadTime = time.time()
        logger.debug("endReadTime is " + str(round(endReadTime, 4)) + " seconds.")

        logger.info("# Calculate average time to find the word 'imperdiet' in a sentence")
        logger.info("Average time to find 'imperdiet' in a sentence if present = getAverageTimePerLine(imperdietSearchTime, sentencesContainingImperdiet)")
        # Calculate average time to find the word 'imperdiet' in a sentence
        averageImperdietSearchTime = getAverageTimePerLine(imperdietSearchTime, sentencesContainingImperdiet)
        logger.debug("Average imperdiet search time: " + str(round(averageImperdietSearchTime, 4)) + " seconds.")

        # Calculate average time to read each line
        logger.info("# Calculate average time to read each line")
        averageTimeToReadLine = getAverageTimePerLine(getElapsedTime(endReadTime, startReadTime), totalLines)
        logger.info("Average time to read each line: " + str(round(averageTimeToReadLine, 4)) + " seconds.")

        # performanceStats = (averageTimeToReadOrWriteLine, averageTimeToFindImperdiet, fileMode)
        # Update tuple containing the performance stats
        logger.info("# performanceStats = (averageTimeToReadOrWriteLine, averageTimeToFindImperdiet, fileMode)")
        performanceStats = (averageTimeToReadLine, averageImperdietSearchTime, fileMode)

        logger.info("End of file-reading process")
    ## END READ OPERATION

    # Close the file we have written to/read from
    logger.info("# Try to close the file we have written to/read from")
    try:
        logger.debug("Calling openFile.close()")
        openFile.close()
    except IOError as ioe:
        logger.exception("Error attempting to close file: " + str(ioe))

    ## Display final stats of log, output 'consoleapp.log' file
    logger.info("# Displaying final stats of log, output 'consoleapp.log' file")

    print("Found " + str(imperdietCount) + " occurrences of the word 'imperdiet'.\n")
    logger.debug("Found " + str(imperdietCount) + " occurrences of the word 'imperdiet'.\n")

    print("There were " + str(sentencesContainingImperdiet) + " sentences containing 'imperdiet'.\n")
    logger.debug("There were " + str(sentencesContainingImperdiet) + " sentences containing 'imperdiet'.\n")

    return performanceStats

# Main application method
def main():
    logger.info("Calling application method now")

    # Start execution time
    startTime = time.time()
    logger.info("Start execution timestamp: " + str(round(startTime, 4)))

    # call our console input function
    try:
        performanceStats = useConsole()
        logger.debug("useConsole() successfully ran.")
    except SystemError as se:
        logger.critical("Something serious is wrong with execution of useConsole(): " + str(se))

    # End execution time
    endTime = time.time()
    logger.info("End execution timestamp: " + str(round(endTime, 4)))

    # Calculate total runtime
    totalRuntime = getElapsedTime(endTime, startTime)
    logger.info("Total runtime: " + str(round(totalRuntime, 4)) + " seconds.")

    printStats = input("Print out overall performance stats for program? Enter 'Y' for 'yes' or anything else for 'no': ")
    if (printStats.lower() == 'y'):
        print("Total execution time = " + str(round(totalRuntime, 4)) + " seconds.\n")
        print("Average time to read or write a line: " + str(round(performanceStats[0], 4)) + " seconds\n")
        print("Average time to find the word 'imperdiet' in a line: " + str(round(performanceStats[1], 4)) + " seconds.")

    logger.info("Program finished.")

## Execute this program by calling the application method
main()
