import logging
import os
import sys
import StringHelper
import StringReplacer


def help():
    print('\nHELP')

    print('\nAvailable commands (case insensitive):')
    print('\nHelp')
    
    print('\nFindFiles [file extension] [path]')
    print('  Example:')
    print('  findfiles txt')

    print('\nFindLongPaths [min length] [path]')
    print('  Example:')
    print('  findlongpaths 123 ./')

    print('\nReplace "string to replace" "new string" [file extension] [path]')
    print('  Example:')
    print('  Replace "string to replace" "new string" txt ./')

    print('\nPath examples:')
    print('  ./')
    print('  C:\\folder1\\folder2')
    
    print('\nExtension examples:')
    print('  txt')
    print('  None') # For any extension

    print('')




# Find all files with given extension at give path
def findFilesWithExtension(path, extension):
    # we shall store all the file names in this list
    fileList = []

    for root, dirs, files in os.walk(path):
        for file in files:
            # append the file if its extension is not specified OR if the extension matches
            if ((not extension) or (extension and file.endswith(extension))):
                # append the file name to the list
                fileList.append(os.path.join(root, file))

    return fileList


def findFilesWithExtensionFromArguments():
    # Resolve values from arguments
    extension = sys.argv[2] if len(sys.argv) > 2 else None
    path = sys.argv[3] if len(sys.argv) > 3 else './'
    # Find files
    files = findFilesWithExtension(path, extension)
    print(*files, sep = '\n')


def findFilesWithExtensionDemo():
    path = './'
    extension = 'py'
    paths = findFilesWithExtension(path, extension)
    print('Found', len(paths), 'files with extension:', extension)
    print(*paths, sep = '\n')




# Find all sub-paths longer than minLength characters
def findLongPaths(path, minLength):
    extension = None
    paths = findFilesWithExtension(path, extension)
    longPaths = StringHelper.filterStringsWithMinLength(paths, minLength)
    longestString = StringHelper.findLongestString(paths)

    print('Found', len(longPaths), 'paths longer than', minLength, 'characters.')
    print('\nLongest path has ', len(longestString), ' characters:\n', longestString, sep='')
    # print(*longFiles, sep = '\n')

    longDirs = map(lambda s: os.path.dirname(s), longPaths)
    uniqueLongDirs = set(longDirs)
    print('\nUnique long directories:')
    print(*uniqueLongDirs, sep = '\n')


def findLongPathsDemo():
    findLongPaths('./', 2)


def findLongPathsFromArguments():
    # Resolve values from arguments
    minLength = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    path = sys.argv[3] if len(sys.argv) > 3 else './'
    findLongPaths(path, minLength)




# Replace string in  all files with given extension at give path
def replaceStringInFilesWithExtension(path, extension, stringToReplace, replacementString):
    files = findFilesWithExtension(path, extension)
    for file in files:
        StringReplacer.replaceStringInFile(file, stringToReplace, replacementString)


def replaceStringInFilesWithExtensionFromArguments():
    # Verify number of mandatory arguments
    if len(sys.argv) < 5:
        logging.error('There must be at least 2 parameters: stringToReplace, replacementString, [extension], [path]')
        printArgumentsAndQuit()

    # Resolve values from arguments
    stringToReplace = sys.argv[2]
    replacementString = sys.argv[3]
    extension = sys.argv[4] if len(sys.argv) > 4 else None
    path = sys.argv[5] if len(sys.argv) > 5 else './'

    # Verify that strings are not empty
    if not stringToReplace or not replacementString:
        logging.error('Empty sting parameter.')
        printArgumentsAndQuit()

    # Replace the string in files
    print('Replacing...')
    replaceStringInFilesWithExtension(path, extension, stringToReplace, replacementString)
    print('Done.')




def executeCommandFromArguments():
    # Verify number of mandatory arguments
    if len(sys.argv) < 2:
        logging.error('There must be at least 1 parameter: Command')
        printArgumentsAndQuit()
    
    # Resolve command
    command = sys.argv[1].lower()
    if command == 'help':
        help()
    elif command == 'findfiles':
        findFilesWithExtensionFromArguments()
    elif command == 'findlongpaths':
        findLongPathsFromArguments()
    elif command == 'replace':
        replaceStringInFilesWithExtensionFromArguments()
    else:
        logging.error('Command not resolved.')
        printArgumentsAndQuit()


def printArgumentsAndQuit():
        print('Number of argument parameters:', len(sys.argv))
        print('Parameters:')
        for arg in sys.argv:
            print(arg)
        help()
        quit()


if __name__ == '__main__':
    executeCommandFromArguments()