import re, glob, os, sys

class RegexSearch:

    # A simple search & replace.
    @staticmethod
    def replace(text, searchReplace, multiLine=True):
        for search, replace in searchReplace:
            if multiLine:
                text = re.sub(search, replace, text, flags=re.M)
            else:
                text = re.sub(search, replace, text)
        return text

    # Searching in a loop until a specific pattern is no longer found.
    @staticmethod
    def deepReplace(text, searchPattern, searchReplace, multiLine=True):
        p = re.compile(searchPattern, flags=re.M)
        while p.search(text):
            for search, replace in searchReplace:
                if multiLine:
                    text = re.sub(search, replace, text, flags=re.M)
                else:
                    text = re.sub(search, replace, text)
        return text

    def searchFile(self, inputFile):
        # set output filename
        path, file = os.path.split(inputFile)
        outputFile = os.path.join(path, "replaced_{0}".format(file))
        # open file and read input text
        with open(inputFile,'r') as f:
            newData = f.read()
        # work on non-empty text
        if newData:
            # search and replace the text
            newData = self.processInputText(newData)
            # save output text in a separate file
            with open(outputFile,'w') as f:
                f.write(newData)
        else:
            print("No data is read.")

    def searchFilesInFolder(self, folder):
        fileList = glob.glob(folder+"/*")
        for file in fileList:
            if os.path.isfile(file):
                self.searchFile(file)

    def processInput(self, inputName):
        # check if user's input is a file or a folder
        if os.path.isfile(inputName):
            self.searchFile(inputName)
        elif os.path.isdir(inputName):
            self.searchFilesInFolder(inputName)
        else:
            print("\""+inputName+"\"", "is not found!")

    def processInputText(self, text):
        # an example of a simple search & replace
#        searchReplace = (
#            ('search1', 'replace1'),
#            ('search2', 'replace2'),
#            ('search3', 'replace3'),
#        )
#        text = self.replace(text, searchReplace)
        # an example of searching in a loop until a search pattern is no longer found.
#        searchPattern = 'pattern'
#        searchReplace = (
#            ('search1', 'replace1'),
#            ('search2', 'replace2'),
#            ('search3', 'replace3'),
#        )
#        text = self.deepReplace(text, searchPattern, searchReplace)
        return text

if __name__ == '__main__':
    inputName = ""
    arguments = sys.argv

    if (len(arguments) > 1):
        inputName = " ".join(arguments[1:])
    else:
        # User Interaction - ask for filename / folder name
        inputName = input("Enter a file / folder name here: ")

    RegexSearch().processInput(inputName)
    
    print("Done! Output file(s) is / are prefixed with 'replaced_'")