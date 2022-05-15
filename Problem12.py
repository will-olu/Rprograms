import itertools

def file_parse(file):
    #reads in file and splits the lines by fasta header
    #into dict (key=fastaID, val=seq)

    f = open(file, 'r') 
    items = f.readlines()    #creates a list from the input file
    final_seqs = {}
    count = 0

    while count < len(items): #loop creating a dictionary and bring strings togehter
        try: #this will try the steps 
            if items[count][0] == '>': #checks if item is fasta header or seq
                temp_list = [] #initalizes temp variables
                temp_str = ""
                init_pos = count
                count += 1

                #augment the count based on the number of iterations through the loop

                while count < len(items) and items[count][0] != '>':
                    #create a temporary list that can be counted through
                    temp_list.append(items[count])
                    #increment the count by one
                    count += 1
                    #for every value in the temp list if the value of "v" is not equal to the initial value at index 0 then add to the temp list
                for v in temp_list:
                    if v[0] != '>':
                        if v[-1] != '\n':
                            #add a new temporary value to the string from the index of v
                            temp_str += v

                        else:
                            temp_str += v[:-1]

                final_seqs.update({items[init_pos][1:-1]: temp_str})
            else:
                #
                count += 1

        except:
            None
    f.close()
    return final_seq

#creation of the overlap graph
def ovrlp_grph(seqs):   #assembles overlap graph
    overlp = []
    #two variables are being used k1 and k2
    #we are usign the package from itertools and calling for the combinations of values
    for k1, k2 in itertools.combinations(seqs, 2):
        #curr_ovr is an empty string
        curr_ovr = []
        #k1 matches the 3 last values and k2 matches the three first values then attach each matching string
        #to the curr_ovr list
        if seq[k1][-3:] == seqs[k2][:3]:
            curr_ovr.append(k1)
            curr_ovr.append(k2)
            
        elif seqs[k2][-3:] == seqs[k1][:3]:
            curr_over.append(k2)
            curr_over.append(k1)
        if len(curr_ovr) > 0:
            overlp.append(curr_ovr)
    return overlp
#creating output
def output(out, ovrlp):
    o = open(out, 'w')
    for i in overlp:
        #write the out string for the value of the string
        o.write(str(i[0]) + ' ' + str(i[1]) + '\n')
    o.close()

out = Rosalind_12_out.txt'
output(out, ovrlp_grph(file_parse('rosalind_grph.txt')))


                
