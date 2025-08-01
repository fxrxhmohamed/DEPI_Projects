def list_of_multiples(num,length):
    lst=[]
    while len(lst)<length:
        for i in range(1, length + 1):
            lst.append(num*i)
    return lst


list_of_multiples(7, 5)
        