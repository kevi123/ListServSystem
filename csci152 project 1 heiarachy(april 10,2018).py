#Kevin Hinojosa Project #1 Heirachy Project
#Csci 152
#This is written in Python
import time #time.asctime( time.localtime(time.time()))

#This project create a heirachy(tree) of organizations. Organizationscan hold organizations or students
#Student can NOT hold other organizations or other students
#
#



#this class holds student information
#the attributes are firstname, lastname, student Id,message and ParentOrganization
#methods fullname returns students fullname
#methods alldata displays every single variable in the class
class Student:
    def __init__(self,first,last,studentId, message, parentOrganization):
        self.first = first
        self.last = last
        self.studentId = studentId
        self.email = first +'-'+ last+ '@FresnoState.com'
        self.message= message
        self.parentOrganization= parentOrganization  #is the index of the parent ordanization. Use orgList[parentOrganization].name to see parent Org name
        
    def fullName(self):
        return'{} {}'.format(self.first, self.last)

    def allData(self):
        return'FirstName:   {}\nLastName:    {}\nStudentI.D.: {}\nEMail:       {}\nMessage:     {}\nParentOrg:   {}'.format(self.first, self.last, self.studentId, self.email, self.message, self.parentOrganization)

##This class holds information for the organization
##method allData prints all information held in the class
#parent lets us know who the parent is. Use orgList[parent].name to see name of parent organization
#children holds a list of every single child. Example FresnoState can have CSCI and ECE as children
class Organization():
    def __init__(self,name):
        self.name = name
        self.parent = "N/A"
        self.children= []

    def allData(self):
        return'OrgName:{}\nParentOrg:{}\nChildrenOrg:{}'.format(self.name, self.parent, self.children)

#x is the current parentOrganization
#this gets called by option and we return an instance class Student
def createStudent(x):
    currentName= input("What is the first name of the student?")
    currentLast= input("What is the last name of the student?")
    currentStudent = Student(currentName, currentLast, 500000, 'NoMail', x)
    return currentStudent


#org is the orglist, x is the current index UNIQUE, y is the parent index
def makeOrganization(org,x,y):
    temp=input("What would you like to name the organization?\n")
    currentOrgLocal=Organization(temp)
    currentOrgLocal.parent=y  #lets write the parent of this org
    org.append(currentOrgLocal)  #add this new org to orglist
    (org[y].children).append(x)  #lets accress parents variable and say who its children are
    #list.index(object)


#prints all organizations,
#parameters x is the orgList that holds all organizations
def displayOrg(x):
    for index in x:
        print("\n|------------|")
        print (index.allData())
        print("|____________|")




#we will delete organization from the list, also remove from parents children
#Parameters x is organization name, y is parent index ,
#deleteThis is the input of which org to delete
# errorBool is bool to handle invalid inputs
def deleteOrg(x,y):  ##add parent parameter y to remove child
    errorBool=True
    index=0
    while(errorBool):
        print("The Organizations are as follows\n")
        displayOrg(x)
        deleteThis=input("Which organization would you like to delete?\n")
        while (index<len(x)):
            if(deleteThis == x[index].name):
                x[y].children.remove(index) #org at parent, call chilren. remove(child)
                del x[index]
                errorBool=False     #do not loop again
                print("Succesfully deleted %s \n" %(deleteThis))
                print("The new list is as follows")
                displayOrg(x)
            else:
                index=index+1
        if(errorBool):
            print("%s org does not exist, Try again.\n"%(deleteThis))


#this permanently deletes the student from the studentlist
#Parameter x is the student list
def deleteStudent(x):
    errorBool=True  #so we can loop if improper input given
    index=0
    while(errorBool):
        print("The students are as follows\n")
        displayStudents(x)
        deleteThis=input("Which student would you like to delete?\n")
        while (index<len(x)):
            if(deleteThis == x[index].first):
                del x[index]  #permanently delete this student
                errorBool=False  #do not loop anymore
                print("Succesfully deleted %s \n" %(deleteThis))
                print("The new list is as follows")
                displayStudents(x)
            else:
                index=index+1
        if(errorBool):
            print("%s student does not exist, Try again.\n"%(deleteThis)) #error message to try again
    


#prints every student and their data,
#Paremeter x is the list
def displayStudents(x):
    for index in x:
        print("\n|--------------------|")
        print (index.allData())
        print("|____________________|")


#This function removesthe parent subscription. sets it to none
#parameter X is studentList
#Note student parent is saved as Int and then set to string None
def unsubscribe(x):
    errorBool= True
  
    while(errorBool):
        index=0
        unsubThis= input("Which User wouldyou like to unsubscribe?")
        unsubFromThis=int (input("Unsubscribe them from what organization?"))##We need to ask user for name of org not parent index number
        while (index <len(x)):
            if (x[index].first == unsubThis and x[index].parentOrganization == unsubFromThis):#this line does not detect truth
                print("TEST matched ==unsubthis==unsubFROmthis")
                x[index].parentOrganization = None
                errorBool=False
                index=index+1
            else:
                index=index+1
        if(errorBool):
               print("TRY again, This user [%s] was not subscribed to [%s]"%(unsubThis,unsubFromThis))


#This subscribe function is near comlplete
#Parameter x is the student list.
# we ask user which student they would like to subscribe to what organization
# we update the student.parentOrganization attribute in this function

#def subscribe(x):
#    errorBool=True  #this repeats the function call if invalid inputs are given
#
#    while(errorBool):
#        index=0
#        subThis= input("Which user wants to subscribe?")
#        subToThis= input("Which Organization do you want to subscribe them to?")
#        while(index<len(x)):
#            if(True):
#                index=index+1
#            else:
#                index=index+1
#        if(errorBool):
#            print("Try Again, This user %s or this organization [%s] does not exist.")
            
#This functions moves us into the the organization we would like to be in
#Parameter x is the organization list
#This also returns the new correct parentOrganization after switching to the new organization
def cd(x):
    errorBool=True

    while(errorBool):
        index=0
        displayOrg(x)
        enterThis=input("Which organization would you like to enter?\n")
        while (index<len(x)):
            if(enterThis == x[index].name):
                #del x[index]   we are not deleting here
                errorBool=False
                print("Succesfully entered %s \n" %(enterThis))
                print("The new list is as follows")
                displayOrg(x)
                level=index
                index=index+1
            else:
                index=index+1
        if(errorBool):
            print("%s org does not exist, Try again.\n"%(enterThis))
    return level


#notify sends an email to students    
#Parameter x is a list of students, y is the parent folder
#this sends message only to the students(aka children) of the current respective organiztion
def notify(x,y):
    message= input("What is the message to send\n")
    for index in x:
        if(index.parentOrganization == y):
            index.message= message


#we pass the current object and add it to the end of theList
#parameter theObject is new instance of student or organization. theList is the respectful list of students or Organizations
def addToList(theObject, theList):
    theList.append(theObject)


#display Text for menu options
def menu():
    option= input("\nWhat would you like to do? \n1)mkorg \n2)create \n3)cd or cd.. \n4)delOrg \n5)delUser \n6)notify \n7)unsubscribe \n8)displayEverything  \n")
    return option



def main():
    ##These are the few initialized variables
    print(time.asctime( time.localtime(time.time()))) # we want to use this to time stamp emails sent
    currentOrgIndex=0   #this is adjusted everytime we change organizations, Unique to every org
    parentIndex=0       #Every org has a parent
    orgList=[Organization("FresnoState")]      #holds heiarchy organizations starts with root FresnoState
    list1=[]#will use these for students
    studentNum=500000     #The students Id start at this number

        #starts here
    print("Welcome to FresnoState")

    while(True):#lets loop menu everytime improper input is give
        print("Current Organization level [%s]"%(orgList[currentOrgIndex].name))
        print("Current Parent organization %s"%(orgList[parentIndex].name))
        option=menu()

        if(option=="mkorg" or option=="1"):
            currentOrgIndex= currentOrgIndex+1  #this increments with every new organization
            print("we entered Make Organization")
            makeOrganization(orgList,currentOrgIndex, parentIndex)
            displayOrg(orgList)
            
        elif (option=="create"or option=="2"):
            student1=createStudent(parentIndex)
            addToList(student1, list1)
            displayStudents(list1)

        elif (option=="delOrg" or option=="3"):
            deleteOrg(orgList,parentIndex)
            print()

        elif (option=="cd" or option=="4"):
            print ("Test entered option==cd")
            print("Test currentOrg is %s" %(orgList[currentOrgIndex].name))
            parentIndex=cd(orgList)
            print("Test currentOrg is now %s" %(orgList[currentOrgIndex].name))
            print("Test parentIndex is now %s" %(orgList[parentIndex].name))
            
        elif (option=="delUser" or option=="5"):
            deleteStudent(list1)

        elif (option=="notify"or option=="6"):
            print("entered option==notify")
            notify(list1,parentIndex)

        elif(option=="unsubscribe" or option=="7"):
            unsubscribe(list1)

        elif (option=="displayEverything" or option=="8"):
            displayOrg(orgList)
            displayStudents(list1)
            print("This is everything created thus far")
            
        else:
            print("Invalid, enter number or word i.e. '1','2','create' ")

main()
