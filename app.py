from tkinter import *
from tkcalendar import *


# Loop until correct file is read from the user
def verifyFile(): 
    flag = TRUE
    while flag:
        fileName = input("Please type the name of your syllabus file: ")

        if(fileName.endswith(".txt")):
            myFile = open(fileName, 'r')
            if(myFile.mode == 'r'):
                print("File opened sucessfully...")
                print("Reading from file...")
                print("")
                flag = FALSE
                return fileName
        else:
            print("Incorrect file type. Program only reads .txt files!")
    
    myFile.close()

# Read from the syllabus file
def readFile(sentFile):
    myFile = open(sentFile, 'r')
    print(myFile.read())

def main():
    file = verifyFile()
    readFile(file)

    # set up GUI window
    # root = Tk()
    # root.title("My Syllabus Calendar")
    # root.geometry("400x400")


    # root.mainloop() # end GUI code






if __name__ == "__main__":
    main()
