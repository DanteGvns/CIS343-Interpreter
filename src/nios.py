import sys

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
        try:
            with open(fileName, "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("Error: That file does not exist, please check your file path.")
    elif arg_count > 1:
        print("Error: too many args")
        print("Correct usage of nios: python src/nios file.nios")
        
        
#run main
if __name__ == "__main__":
    main()
