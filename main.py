from operator import contains
import sys

one = chr(66)
two = chr(70)
categories = []
tasks=[]
ID = 0
catID = 0

class Category:
    def __init__(self, id = catID , name = ""):
        global catID
        catID+=1
        self.id = id
        self.name = name

    def __str__(self):
        return f"id : {self.id} name : {self.name}"

    def __eq__(self, other):
        return self.id == id

class Task:
    def __init__(self, id = ID, name="no name", description = "no descp.", priotry = "no pri.", due= "no due", categories = "no category", done="F"):
        global ID
        ID +=1
        self.id = id
        self.name = name
        self.description = description
        self.priotry = priotry
        self.due = due
        self.categories = categories
        self.done = done

    def __eq__(self, other):
       return self.id == other.id
    
def menu():
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Tasks as Done")
    print("4. Remove Tasks")
    print("5. Save To File")
    print("6. Load from File")
    print("7. Edit Categories")
    print("8. Show Categories")
    print("-1. Exit")

def loop():
    menu()
    selection = input("Please Enter The Number Your Choose: ")
    if(selection == "1"):
        addTask()
    elif(selection == "2"):
        listTasks(True)
    elif(selection == "3"):
        markAsDone()
    elif(selection == "4"):
        removeTasks()
    elif(selection == "5"):
        saveToFile()
    elif(selection == "6"):
        loadFromFile()
    elif(selection == "7"):
        editCategories()
    elif(selection == "8"):
        showCategories()
    elif(selection == "-1"):
        sys.exit()

def addTask():
    """
    This Function Add Task to The Tasks List"""
    name = input("Enter The Name: ")
    description = input("Enter The Description: ")
    priotry = input("Enter The Priotry: ")
    due = input("Enter The Due: ")
    categories_ = input("Enter The Categorie: ")
    if(not contains(categories, categories_)):
        addCategory(categories_)
    done = input("Enter The Done:(T/F) ")
    
    task = Task(ID, name, description, priotry, due, categories_,done)
    tasks.append(task)
    print("Task Added Successfully")

def listTasks(filter = False):
    if(len(tasks) == 0):
        print("There is no tasks")
        return False
    else :
        for task in tasks:
            print("ID: {}\nName: {}\nDescription: {}\nPriotry: {}\nDue: {}\nCategories: {}\nDone: {}".format(task.id, task.name, 
                                                                                                             task.description, task.priotry,    
                                                                                                            task.due, task.categories, task.done))
        if(filter):
            filterMenu()
        
        return True
def markAsDone():
    if(listTasks()):
        id_ = input("Enter The ID of The Task: ")
        flag = False
        for task in tasks:
            print("flag 1 {}".format(task.id))
            if(str(task.id) == id_):
                task.done = "T"
                print("Task Marked as Done Successfully")
                flag = True
                break
        if(not flag):
            print("Task Not Found")
def removeTasks():
    if(listTasks()):
        id = input("Enter The ID of The Task: ")
        flag = False
        for task in tasks:
            if(str(task.id) == id):
                tasks.remove(task)
                print("Task Removed Successfully")
                flag = True
                break
        if(not flag):
            print("Task Not Found")
def saveToFile():
    pass
def loadFromFile():
    pass

def editCategories():
    showCategories()
    selection = input("Please Enter The Number You Want To Edit, If you want a new category then press -1: ")
    if(selection == "-1"):
        addCategory()
    else:
        categoryEditMenu()

def categoryEditMenu():
        while(True):
            print("1. Remove Category")
            print("2. Edit the name of a category")
            print("3. Remove Multiple Categories")
            print("-1. Return to main menu")
            selection2 = input("Please Enter The Number Your Choose: ")
            if(selection2 == 1):
                removeCat()
                break

            elif(selection2 == 2):
                editNameCat()
                break

            elif(selection2 == 3):
                removeMultipleCats()
                break

            elif(selection2==-1):
                break
            else:
                print("wrong choose.")           
def removeMultipleCats():
    numbers = input("gimme numbers with comma between them: ")
    nums = numbers.split(", ")
    map(removeCat,nums)

def editNameCat():
    id =input("Gimme id : ")
    flag = False
    for cat in categories:
        if(cat.id == id):
            rem = Category(cat.id, cat.name)
            newName = input(f"old name : {rem.name}\n gimme new name : ")
            categories.remove(rem)
            rem.name = newName
            categories.append(rem)
            flag = True
            print("successful")
            break
    if(not flag):
        print("couldn't find. try again.")
        showCategories()



def removeCat(id = "-1"):
    while(True):
        if(id =="-1" ):
            id =input("Gimme id : ")
        flag = False
        for cat in categories:
            if(cat.id == id):
                rem = Category(cat.id, cat.name)
                categories.remove(rem)
                flag = True
                break
        if(flag):
            break
        else:
            print(f" id : {id} couldn't find. try again.")
            showCategories()



def showCategories():
    for cat in categories:
        print(cat)
def addCategory(name = ""):
    if(name == ""):
        name = input("Please input the new categorys name: ")
    
    newGuy = Category(catID,name)
    if(not contains(categories, newGuy)):
        categories.append(newGuy)

def main():
    print("Welcome To The To Do system")
    while(True):
        loop()
def filterMenu():
    while(True):
        print("1. Filter By Name")
        print("2. Filter By Description")
        print("3. Filter By Priotry")
        print("4. Filter By Due")
        print("5. Filter By Categories")
        print("6. Filter By Done")
        print("-1. Return To Main Menu")
        selection = input("Please Enter The Number Your Choose: ")
        if(selection == "1"):
            filterByName()
            break
        elif(selection == "2"):
            filterByDescription()
            break
        elif(selection == "3"):
            filterByPriotry()
            break
        elif(selection == "4"):
            filterByDue()
            break
        elif(selection == "5"):
            filterByCategories()
            break
        elif(selection == "6"):
            filterByDone()
            break
        elif(selection == "-1"):
            break
        else:
            print("Please Enter a Valid Number")

def filterByName():
    flag = False
    srcName = input("Please Enter The Name: ")
    for task in tasks:
        if(contains(task.name, srcName)):
            print("ID: {}\nName: {}\nDescription: {}\nPriotry: {}\nDue: {}\nCategories: {}\nDone: {}".format(task.id, task.name, 
                                                                                                             task.description, task.priotry,    
                                                                                                            task.due, task.categories, task.done))
            flag= True
    if(flag != True):
        print("Couldn't found!")
    


def filterByDescription():
    flag = False
    srcName = input("Please Enter The Description: ")
    for task in tasks:
        if(contains(task.description, srcName)):
            print("ID: {}\nName: {}\nDescription: {}\nPriotry: {}\nDue: {}\nCategories: {}\nDone: {}".format(task.id, task.name, 
                                                                                                             task.description, task.priotry,    
                                                                                                            task.due, task.categories, task.done))
            flag= True
    if(flag != True):
        print("Couldn't found!")


def filterByPriotry():
    flag = False
    srcName = input("Please Enter The Priotry: ")
    for task in tasks:
        if(contains(task.priotry, srcName)):
            print("ID: {}\nName: {}\nDescription: {}\nPriotry: {}\nDue: {}\nCategories: {}\nDone: {}".format(task.id, task.name, 
                                                                                                             task.description, task.priotry,    
                                                                                                            task.due, task.categories, task.done))
            flag= True
    if(flag != True):
        print("Couldn't found!")


def filterByDue():
    flag = False
    srcName = input("Please Enter The Due Date (dd/mm/yyyy): ")
    for task in tasks:
        if(contains(task.due, srcName)):
            print("ID: {}\nName: {}\nDescription: {}\nPriotry: {}\nDue: {}\nCategories: {}\nDone: {}".format(task.id, task.name, 
                                                                                                             task.description, task.priotry,    
                                                                                                            task.due, task.categories, task.done))
            flag= True
    if(flag != True):
        print("Couldn't found!")


def filterByCategories():
    flag = False
    srcName = input("Please Enter The Categories with a comma between them: ")
    srcNames = []
    srcNames = srcName.split(",")
    for task in tasks:
        if(contains(task.due, srcNames)):
            print("ID: {}\nName: {}\nDescription: {}\nPriotry: {}\nDue: {}\nCategories: {}\nDone: {}".format(task.id, task.name, 
                                                                                                             task.description, task.priotry,    
                                                                                                            task.due, task.categories, task.done))
            flag= True
    if(flag != True):
        print("Couldn't found!")



def filterByDone():
    flag = False
    srcName = input("Please Enter The Done Statement: ")
    for task in tasks:
        if(srcName == task.done or srcName == task.done.lower() or srcName == task.done.upper()):
            print("ID: {}\nName: {}\nDescription: {}\nPriotry: {}\nDue: {}\nCategories: {}\nDone: {}".format(task.id, task.name, 
                                                                                                             task.description, task.priotry,    
                                                                                                            task.due, task.categories, task.done))
            flag= True
    if(flag != True):
        print("Couldn't found!")

    
main()
