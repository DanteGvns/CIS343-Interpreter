import sys
from token import Token
from token import Number
def main():
    #remove 1 since 0 is the program itself
    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print("REPL mode")
        try:
            #loop always getting user input
            while True:
                userInput = input()
                print(userInput)

        #exit the program with Ctrl + C
        except KeyboardInterrupt:
            sys.exit(0)

    elif arg_count == 1:
        #try to look for and file by the name of the second Arg
        fileName = sys.argv[1]
        scanFile(fileName)

    elif arg_count > 1:
        print("Error: too many args")
        print("Correct usage of nios: python src/nios file.nios")

def scanFile(inputFile):
    try:
        with open(inputFile, "r") as file:
            String = ""
            y = 1
            while(line := file.readline()):
                newToken = Token(y, "token")
                lineNumber = newToken.getLineNumber()
            
                String = String + line.replace("\n", "") + "\n" + lineNumber  + "\n"
                y += 1

            # while(char := file.read(1)):
            #     String = String + char + "."
            # content = file.read()
            # print(content)
    except FileNotFoundError:
        print("Error: That file does not exist, please check your file path.")     
    print(String)    
    newNumber = Number(3, 14)
    print(newNumber.getType())
#run main
if __name__ == "__main__":
    main()
