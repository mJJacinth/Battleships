lst=[90,87,372,290,189]
def big(lst):
    for i in range(len(lst)):
        m=lst[i]
        for j in range(0,len(lst)):
            if m > lst[j]:
                m=m
            else:
                m=lst[j]
    return m
print (big(lst))