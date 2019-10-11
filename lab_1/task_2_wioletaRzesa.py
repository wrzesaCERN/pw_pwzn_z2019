def task_2():
    ii=1
    s=''
    print(r"'''")
    while ii < 6:
        print('*' * ii)
        ii+=1
        s+='*'*ii
    while ii > 0:
        print('*' * ii)
        ii-=1
        s+='*'*ii
    print(r"'''")
    return s

assert task_2()

