def CheckPrime(No):
    count = 0

    for i in range(2,No):
        if No % i == 0:
            count = count + 1
            break

    if count == 1:
        return 
    else:
        return No