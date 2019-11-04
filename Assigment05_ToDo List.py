# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Qiming Jin,2019/11/02,Modify):
# RRoot,1.1.2030,Created started script
# QJin,11.02.2019,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None
strData = 'ToDo list.txt'
dicRow = {}
lstTable = []
strChoice = ''

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
objFile=open(strData,"r")
for row in objFile:
    lstRow=row.split(",")
    dicRow={"Task":lstRow[0],"Priority":lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
     for objRow in lstTable:
       print(objRow)
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask=input("Please add the task: ")
        strPriority=input("Please add the priority: ")
        dicRow={"Task":strTask,"Priority":strPriority.strip()}
        lstTable.append(dicRow)
        print("New item is added!")
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        strTask=input("Remove which task?: ")
        strPriority=input("What's the priority?: ")
        dicRow={"Task":strTask,"Priority":strPriority.strip()}
        if dicRow in lstTable:
            lstTable.remove(dicRow)
            print("Item is removed!")
        else:
            print(strTask,",",strPriority,"isn't in the list.")
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile=open(strData,"w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"]+","+dicRow["Priority"]+'\n')
        objFile.close()
        print("Data was saved!")
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
