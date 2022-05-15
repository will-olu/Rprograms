def powerFunction(base, power_num):
    result = 1
    for index in range(power_num):
        result = result * base
    return result

print(powerFunction(10, 3))


        
