#Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

#Read in the file 
file = open(r"C:\Users\willi\Downloads\rosalind_long (1).txt", "r")
#create mat a list that is empty that will be filled with the strings
mat = []
str1 = file.read() #this will allow us to parse the file
str1 = str1.replace("Rosalind_", "") #replacing the Rosalind file with a blank
str1 = str1.replace("\n", "") #replacing the new line with a blank
str1 = ''.join([i for i in str1 if not i.isdigit()]) #joining the strings and ignoring the numbers
mat = str1.split(">")#splits strings at the > of the Rosalind files
mat.remove("")#removes the spaces made


def long(mat, second=''):#oursecond value is an empty string 
    if (len(mat) == 0):
        return second #return empty string

    elif (len(second) == 0): #length of the emptry string is 0
        second = mat.pop(0)# pop the mat
        return long(mat, second)# return both the mat and second

    else:
        for i in range(len(mat)): #i value in the range of values in the mat will now be parsed
            a = mat[i] #simple "a" variable that will be used to help parse and edit the mat string value
            for j in range(len(a) // 2): #takes half of the length of the a value
                c = len(a) - j #c value will take the length of j - a, which removes half of the a length
                if second.startswith(a[j:]):
                    mat.pop(i)
                    return long(mat, a[:j] + second)#returns the other list after popping the other list
                if second.endswith(a[:c]):
                    mat.pop(i)
                    return long(mat, second + a[c:])#returns the values that are present in everything that was found after poping the second lsit
print(long(mat))


