
G={'Rachel':['Ross','Monica'], 'Ross':['Rachel','Monica'], 'Monica':['Rachel','Ross'], 'Jon Snow':['Daenerys','Sansa','Arya'], 'Daenerys':['Jon Snow','Sansa','Arya','Khal Drogo'], 'Sansa':['Jon Snow','Daenerys','Arya'], 'Arya':['Jon Snow','Daenerys','Sansa'], 'Khal Drogo':['Daenerys'], 'Cersei':['Jaime'], 'Jaime':['Cersei'], 'Bart':['Milhouse'], 'Milhouse':['Bart','Lisa'], 'Lisa':['Milhouse'], 'Leslie':['Ron','Ann','Ben'], 'Ron':['Leslie'], 'Ben':['Leslie','Ann'], 'Ann':['Leslie','Ben'],}

from array import *

def searchingAlgorithm(binaryOutputSet,transversingValue): #creating a searching algrithm that goes through the set of values
    cols=len(binaryOutputSet[0]) # creating values to 
    valueSet=[] #creating a set of values
    valueSet.append(transversingValue) #appending the value that is being added and is going through the set
    for secondaryTransversal in range(0,cols): # created a for loop with a range to include the length of our strings and the 
        if(binaryOutputSet[transversingValue][secondaryTransversal]==1):  #creating a conditional loop that                  
            valueSet.append(secondaryTransversal);
    return valueSet       
                

   
binaryOutputSet=[[0,1,1,0,0,0],[1,0,1,0,0,0],[1,1,0,0,0,1],[0,1,0,0,1,0],[0,0,0,1,0,0],[0,0,1,0,0,0]]           
request =int(input("please enter your number:")) # command to ask for input with integer input
newSet=[] # create a set for
transversingValue=len(binaryOutputSet) # Getting length of the binary set
setLength=len(binaryOutputSet[0]) # length of the set in the binary
for newValue in range(0,transversingValue):
    start=0
    for secondaryTransversal in range(0,setLength): # transeversing through this set
        start=start+binaryOutputSet[newValue][secondaryTransversal]                        #finds friends who know each other equal to number in the new set
    if(start>= request-1): # creating a conditional to create a starting point
        newSet.append(newValue) #appending the new value
       
               
secondarySet=[]  #creating a set to house new values 
primarySet=[] # set to be printed
for newValue in newSet: 
    secondarySet.append(searchingAlgorithm(binaryOutput,newValue))            #searches for friends names

transversingValue=len(secondarySet) # the length will be the limit that we have on transversing
setLength=len(secondarySet[0]) #
for newValue in range(0,transversingValue):
    for thirdTransversal in range (newValue+1,transversingValue):
        for secondaryTransversal in range(0,setLength):
            if(secondarySet[newValue][secondaryTransversal]==secondarySet[thirdTransveral][secondaryTransversal]):  # Conditional searches the values to see if there is similarity
                if secondarySet[newValue][secondaryTransversal] not in primarySet: #set conditional to restrict values not in the primary set
                    primarySet.append(secondarySet[newValue][secondaryTransversal]) #appending the correct values to be printed
    
        
            
print("The friends with common",request," friends")               
print(primarySet)
