import re

#open the file
file = open(r'C:/Users/willi/Downloads/rosalind_gc (5).txt')

#create a list of sequences with the readlines
sequence = file.readlines()

#create an empty list of names
name =[]

#create an empty list of scores, the scores will be the max value for the GC content
score =[]

#create a temp list
temp = []

#create a seq list
seq = []

#the length of lines initialized to 1 minus the total length of lines
lengthlines = len(sequence)- 1

#for loop for lines in the sequence
for line in sequence:

    #this conditional finds the start of the each line by matching the > 
    if re.match(">",line):
        
        #removing the carrot at the beginning
        name.append(line.replace(">",""))
        
        #join the new blank spaces into a temp list 
        if temp:
            #appending a value from the temp to the seq list
            seq.append("".join(temp))
            temp =[]
            
    #conditional to join the temp values         
    else:
        #if the index of lengthlines in the sequence equal to the line 
        if sequence[lengthlines]==line:

            #then append the line into the temporary file
            temp.append(line)

            #join those sequences with no space and add them to the seq list
            seq.append("".join(temp))
            
        else:
            #or continue to append to the line function
            temp.append(line)


#for loop to iterate over the ACTG in the seq
#this for loop looks at the entire range of the seq list
for i in range(0,len(seq)):

    #length counts the entire seq value index by index
    length = len(seq[i]) -  seq[i].count("\n") #numerical len subtracting the count function

    #append the GC value for each sequence and multiple it by 100 to get a percentage
    score.append((seq[i].count("C")+seq[i].count("G"))/length*100)

#maxvalue the gc content with the highest score and value
maxvalue = score.index(max(score))

#take the name associated with the max value
print(name[maxvalue])

#rounding the values
print(round(score[maxvalue],6))

#closing the file
file.close()
                 
               
                    
            
    
