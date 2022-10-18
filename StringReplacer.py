def replaceStringInFile(file, stringToReplace, replacementString):
    # read input file
    fin = open(file, "rt")
    # read file contents to string
    data = fin.read()
    # number of ocurencies of stringToReplace
    ocurencies = data.count(stringToReplace)
    if (ocurencies > 0):
        print("Replacing", ocurencies, "string(s) in file:", file)
        # replace all occurrences of the required string
        data = data.replace(stringToReplace, replacementString)
    # close the input file
    fin.close()

    # Save modified text to the original file
    if (ocurencies > 0):
        # open the input file in write mode
        fin = open(file, "wt")
        # overrite the input file with the resulting data
        fin.write(data)
        # close the file
        fin.close()

