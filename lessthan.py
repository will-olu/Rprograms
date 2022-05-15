
arr = [-1, 2, 3, -3, 5, 6, -7]

def plusMinus(arr):
    for a in arr:
        #create a conditional that evaluates the number of values less than 0
        if (a < 0):
            #count the number of values less than 0
            count = 0
            count += 1
            print(count)


print(plusMinus(arr))
