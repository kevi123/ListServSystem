Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: /home/kevin/Documents/CSCI152 Project 1/csci152 project 1 heiarachy.py 
Mon Apr  9 23:40:40 2018
Welcome to FresnoState
Current Organization level [FresnoState]
Current Parent organization FresnoState

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
mkorg
we entered Make Organization
What would you like to name the organization?
CSM

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[]
|____________|
Current Organization level [CSM]
Current Parent organization FresnoState

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
mkorg
we entered Make Organization
What would you like to name the organization?
Lyles

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[]
|____________|
Current Organization level [Lyles]
Current Parent organization FresnoState

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
cd
Test entered option==cd
Test currentOrg is Lyles

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[]
|____________|
Which organization would you like to enter?
csm
csm org does not exist, Try again.


|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[]
|____________|
Which organization would you like to enter?
CSM
Succesfully entered CSM 

The new list is as follows

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[]
|____________|
Test currentOrg is now Lyles
Test parentIndex is now CSM
Current Organization level [Lyles]
Current Parent organization CSM

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
mkorg
we entered Make Organization
What would you like to name the organization?
MATH

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[3]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[]
|____________|

|------------|
OrgName:MATH
ParentOrg:1
ChildrenOrg:[]
|____________|
Current Organization level [MATH]
Current Parent organization CSM

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
mkorg
we entered Make Organization
What would you like to name the organization?
CSCI

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[3, 4]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[]
|____________|

|------------|
OrgName:MATH
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:CSCI
ParentOrg:1
ChildrenOrg:[]
|____________|
Current Organization level [CSCI]
Current Parent organization CSM

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
cd
Test entered option==cd
Test currentOrg is CSCI

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[3, 4]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[]
|____________|

|------------|
OrgName:MATH
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:CSCI
ParentOrg:1
ChildrenOrg:[]
|____________|
Which organization would you like to enter?
Lyles
Succesfully entered Lyles 

The new list is as follows

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[3, 4]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[]
|____________|

|------------|
OrgName:MATH
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:CSCI
ParentOrg:1
ChildrenOrg:[]
|____________|
Test currentOrg is now CSCI
Test parentIndex is now Lyles
Current Organization level [CSCI]
Current Parent organization Lyles

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
mkorg
we entered Make Organization
What would you like to name the organization?
ECE

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[3, 4]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[5]
|____________|

|------------|
OrgName:MATH
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:CSCI
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:ECE
ParentOrg:2
ChildrenOrg:[]
|____________|
Current Organization level [ECE]
Current Parent organization Lyles

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
cd
Test entered option==cd
Test currentOrg is ECE

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[3, 4]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[5]
|____________|

|------------|
OrgName:MATH
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:CSCI
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:ECE
ParentOrg:2
ChildrenOrg:[]
|____________|
Which organization would you like to enter?
CSCI
Succesfully entered CSCI 

The new list is as follows

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[3, 4]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[5]
|____________|

|------------|
OrgName:MATH
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:CSCI
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:ECE
ParentOrg:2
ChildrenOrg:[]
|____________|
Test currentOrg is now ECE
Test parentIndex is now CSCI
Current Organization level [ECE]
Current Parent organization CSCI

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
creat
Invalid, enter number or word i.e. '1', 'create' 
Current Organization level [ECE]
Current Parent organization CSCI

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
create
What is the first name of the student?Alex
What is the last name of the student?A

|--------------------|
FirstName:   Alex
LastName:    A
StudentI.D.: 500000
EMail:       Alex-A@FresnoState.com
Message:     NoMail
|____________________|
Current Organization level [ECE]
Current Parent organization CSCI

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
create
What is the first name of the student?Elizabeth
What is the last name of the student?E

|--------------------|
FirstName:   Alex
LastName:    A
StudentI.D.: 500000
EMail:       Alex-A@FresnoState.com
Message:     NoMail
|____________________|

|--------------------|
FirstName:   Elizabeth
LastName:    E
StudentI.D.: 500000
EMail:       Elizabeth-E@FresnoState.com
Message:     NoMail
|____________________|
Current Organization level [ECE]
Current Parent organization CSCI

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
create
What is the first name of the student?Kishan
What is the last name of the student?K.

|--------------------|
FirstName:   Alex
LastName:    A
StudentI.D.: 500000
EMail:       Alex-A@FresnoState.com
Message:     NoMail
|____________________|

|--------------------|
FirstName:   Elizabeth
LastName:    E
StudentI.D.: 500000
EMail:       Elizabeth-E@FresnoState.com
Message:     NoMail
|____________________|

|--------------------|
FirstName:   Kishan
LastName:    K.
StudentI.D.: 500000
EMail:       Kishan-K.@FresnoState.com
Message:     NoMail
|____________________|
Current Organization level [ECE]
Current Parent organization CSCI

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
create
What is the first name of the student?Khushad
What is the last name of the student?K.

|--------------------|
FirstName:   Alex
LastName:    A
StudentI.D.: 500000
EMail:       Alex-A@FresnoState.com
Message:     NoMail
|____________________|

|--------------------|
FirstName:   Elizabeth
LastName:    E
StudentI.D.: 500000
EMail:       Elizabeth-E@FresnoState.com
Message:     NoMail
|____________________|

|--------------------|
FirstName:   Kishan
LastName:    K.
StudentI.D.: 500000
EMail:       Kishan-K.@FresnoState.com
Message:     NoMail
|____________________|

|--------------------|
FirstName:   Khushad
LastName:    K.
StudentI.D.: 500000
EMail:       Khushad-K.@FresnoState.com
Message:     NoMail
|____________________|
Current Organization level [ECE]
Current Parent organization CSCI

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
notify
entered option==notify
What is the message to send
Hello and welcome to the Computer Science Club!!
Current Organization level [ECE]
Current Parent organization CSCI

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
cd
Test entered option==cd
Test currentOrg is ECE

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[3, 4]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[5]
|____________|

|------------|
OrgName:MATH
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:CSCI
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:ECE
ParentOrg:2
ChildrenOrg:[]
|____________|
Which organization would you like to enter?
MATH
Succesfully entered MATH 

The new list is as follows

|------------|
OrgName:FresnoState
ParentOrg:N/A
ChildrenOrg:[1, 2]
|____________|

|------------|
OrgName:CSM
ParentOrg:0
ChildrenOrg:[3, 4]
|____________|

|------------|
OrgName:Lyles
ParentOrg:0
ChildrenOrg:[5]
|____________|

|------------|
OrgName:MATH
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:CSCI
ParentOrg:1
ChildrenOrg:[]
|____________|

|------------|
OrgName:ECE
ParentOrg:2
ChildrenOrg:[]
|____________|
Test currentOrg is now ECE
Test parentIndex is now MATH
Current Organization level [ECE]
Current Parent organization MATH

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
create
What is the first name of the student?Sean
What is the last name of the student?S.

|--------------------|
FirstName:   Alex
LastName:    A
StudentI.D.: 500000
EMail:       Alex-A@FresnoState.com
Message:     Hello and welcome to the Computer Science Club!!
|____________________|

|--------------------|
FirstName:   Elizabeth
LastName:    E
StudentI.D.: 500000
EMail:       Elizabeth-E@FresnoState.com
Message:     Hello and welcome to the Computer Science Club!!
|____________________|

|--------------------|
FirstName:   Kishan
LastName:    K.
StudentI.D.: 500000
EMail:       Kishan-K.@FresnoState.com
Message:     Hello and welcome to the Computer Science Club!!
|____________________|

|--------------------|
FirstName:   Khushad
LastName:    K.
StudentI.D.: 500000
EMail:       Khushad-K.@FresnoState.com
Message:     Hello and welcome to the Computer Science Club!!
|____________________|

|--------------------|
FirstName:   Sean
LastName:    S.
StudentI.D.: 500000
EMail:       Sean-S.@FresnoState.com
Message:     NoMail
|____________________|
Current Organization level [ECE]
Current Parent organization MATH

What would you like to do? 
1)create 
2)mkorg 
3)cd or cd.. 
4)delOrg 
5)delUser 
6)notify 
7)DisplayEverything  
