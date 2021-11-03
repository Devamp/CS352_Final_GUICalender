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
    cal = Calendar(root, selectmode="day", year=2021, month=12,)
    cal.pack(pady=20)

    # open file in read mode
    myFile = open(sentFile, 'r')

    eventList = [] # stores list of events created
    i = 0 # increment counter used for event ID

    for line in myFile.readlines(): # read line by line and create a calender event for each event
        list = line.split("-")
        c = cal.calevent_create(datetime(int(list[3]),int(list[1]),int(list[2])), list[4], "Anything")
        eventList.append(str(i) + " - " + (list[1] + "/" +list[2] + "/" + list[3].replace("2021","21"))) # format events
        i = i+1  # increment event id
    
    def returnEvent(): # command function for display button
        dateAsked = cal.get_date() # get selected date

        for date in eventList: # loop to find see if asked date matches event dates created from eventList

            if (date[4:12] == dateAsked): # if the selected date matches the event dates
                mylable.config(text="    Event: " + cal.calevent_cget(int(date[0]),"text")) # print asked event given the id
                dueLable.config(text="  Due on: " + dateAsked)
                
    
                
                

    
    # set up display button
    displayButton = Button(root, text="Display", background="grey", command=returnEvent)
    displayButton.pack(pady=20)

    # set up output lables
    mylable = Label(root, text="Event Here")
    dueLable = Label(root, text="Due Date Here")

    mylable.pack()
    dueLable.pack(pady=20)

    dueLable.config(bg="white", width="20")
    dueLable.config(font=("Arial", 12))
    mylable.config(bg="white", width="40")
    mylable.config(font=("Arial", 14))

    root.mainloop() # end GUI loop

def main():
    file = verifyFile()
    simulate(file)


if __name__ == "__main__":
    main()
