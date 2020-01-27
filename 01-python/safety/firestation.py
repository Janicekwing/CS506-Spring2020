def draw_firestation(length=20):


    for i in range(length):
        print('_', end = '')

    print('\n|'+' '*((length-len('firestation'))//2), end = '')
    print('FIRESTATION',end='')
    print(' '*((length-len('firestation'))//2)+'|\n', end = '')

    for i in range(length):
        print('_', end = '')

    for i in range(5):
        print('|'+' '*(length-1)+'|')

    for i in range(length):
        print('_', end = '')

    return
