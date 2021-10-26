from datetime import datetime
from tkinter import *
from tkinter.ttk import Style
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
                print("### CALENDAR GUI IS OPEN ###")
                flag = FALSE
                return fileName
        else:
            print("Incorrect file type. Program only reads .txt files!")
    
    myFile.close()


# Read from the syllabus file
def simulate(sentFile):
    
    # set up GUI window
    root = Tk()
    root.title("Event Calendar")
    root.geometry("400x400")
    root.configure(background= "#90E7FD")
    
    # Set up calendar to display
    cal = Calendar(root, selectmode="day", year=2021, month=10,)
    cal.pack(pady=20)

    # open file in read mode
    myFile = open(sentFile, 'r')
    
    # read line by line and create a calender event for each event
    for line in myFile.readlines():
        list = line.split("-")
        #eventList = []
        c = cal.calevent_create(datetime(int(list[2]),int(list[0]),int(list[1])), list[3], "Anything")
        #eventList.append(c)

    def returnEvent():
        mylable.config(text="Event Due: " + cal.calevent_cget(c,"text"))
        #mylable.config(text=cal.get_date())

    # set up display button
    displayButton = Button(root, text="Display", background="grey", command=returnEvent)
    displayButton.pack(pady=20)

    # set up output lable
    mylable = Label(root, text="<Output Here>")
    mylable.pack(pady=20)



    root.mainloop() # end GUI



def main():
    file = verifyFile()
    simulate(file)


if __name__ == "__main__":
    main()
