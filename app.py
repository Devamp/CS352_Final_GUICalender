from datetime import datetime
from tkinter import *
from tkinter.ttk import Style
from tkcalendar import *
import os


# Loop until correct file is read from the user
def verifyFile(): 
    flag = TRUE
    while flag:
        fileName = input("Please type the name of your syllabus file: ")

        if(fileName.endswith(".txt")):
            if os.path.isfile(fileName): # check to make sure given file actually exists
                myFile = open(fileName, 'r')
                print("File opened sucessfully...")
                print("Reading from file...")
                print("")
                flag = FALSE
                return fileName
            else:
                print ("Given file does not exist.")
        else:
            print("Incorrect file type. Program only reads .txt files!")

# Read from the syllabus file
def create(sentFile):
    
    # set up GUI window
    root = Tk()
    root.title("Event Calendar")
    root.geometry("400x400")
    root.configure(background= "#90E7FD")

    # Set up calendar to display
    cal = Calendar(root, selectmode="day", year=2021, month=12, bordercolor="black", selectbackground="red", 
    headerbackground="white",  )
    cal.pack(pady=10)

    # open file in read mode
    myFile = open(sentFile, 'r')

    eventList = [] # stores list of events created
    i = 0 # increment counter used for event ID

    for line in myFile.readlines(): # read line by line and create a calender event for each event
        list = line.split("-")
        c = cal.calevent_create(datetime(int(list[3]),int(list[1]),int(list[2])), list[4], "Anything")
        tempDate = list[3]
        eventList.append(str(i) + " - " + (list[1] + "/" +list[2] + "/" + list[3].replace(tempDate,tempDate[2:4]))) # format events
        i = i+1  # increment event id
    
    def return_event(): # command function for display button
        dateAsked = cal.get_date() # get selected date
        for date in eventList: # loop to find see if asked date matches event dates created from eventList
            
            # This condition checks to see if cal events are > 10, if so we need to adjust the spacing
            if (int(date[0:2]) >= 10):
                compareDate = date[5:14]
                twoDigits = True
            else:
                compareDate = date[4:12] 
                twoDigits = False

            if (compareDate == dateAsked): # if the selected date matches the event dates
                if (twoDigits):
                    mylable.config(text="    Event: " + cal.calevent_cget(int(date[0:2]),"text")) # print asked event given the id
                    dueLable.config(text="  Scheduled For: " + dateAsked)
                elif(twoDigits == False):
                    mylable.config(text="    Event: " + cal.calevent_cget(int(date[0]),"text")) # print asked event given the id
                    dueLable.config(text="  Scheduled For: " + dateAsked)
                break
            else :
                mylable.config(text="    No events for selected date!") # print asked event given the id
                dueLable.config(text="  ")
                
            
    def del_event():
        toDelete = cal.get_date()
        for date in eventList:
            # This condition checks to see if cal events are > 10, if so we need to adjust the spacing
            if (int(date[0:2]) >= 10):
                compareDate = date[5:14]
                twoDigits = True
            else:
                compareDate = date[4:12] 
                twoDigits = False

            if (compareDate == toDelete): # if the selected date matches the event dates
                if (twoDigits):
                    cal.calevent_remove(int(date[0:2])) # delete the cal event
                    eventList.remove(date) # and remove it from the events list

                    mylable.config(text=" Event deleted successfully") # print asked event given the id
                    dueLable.config(text="  ")

                elif(twoDigits == False):
                    cal.calevent_remove(int(date[0]))
                    eventList.remove(date)

                    mylable.config(text=" Event deleted successfully") # print asked event given the id
                    dueLable.config(text="  ")
                break
  
    # set up display button
    displayButton = Button(root, text="Display", background="grey", command=return_event)
    displayButton.pack(pady=5)
    displayButton.pack(padx=0)

    # set up delete button
    deleteButton = Button(root, text="Delete Event", background="grey", command=del_event)
    deleteButton.pack(padx=0)
    deleteButton.pack(pady=5)

    # set up output lables
    mylable = Label(root, text="Event Here")
    dueLable = Label(root, text="Due Date Here")

    mylable.pack()
    dueLable.pack(pady=20)

    dueLable.config(bg="white", width="20")
    dueLable.config(font=("Arial", 12))
    mylable.config(bg="white", width="30")
    mylable.config(font=("Arial", 14))

    root.mainloop() # end GUI loop

def main():
    file = verifyFile()
    create(file)

if __name__ == "__main__":
    main()
