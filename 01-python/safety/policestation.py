def draw_policestation(length=20):


    for i in range(length):
        print('_', end = '')

    print('\n|'+' '*((length-len('policestation'))//2), end = '')
    print('POLICESTATION',end='')
    print(' '*((length-len('policestation'))//2)+'|\n', end = '')

    for i in range(length):
        print('_', end = '')

    for i in range(5):
        print('|'+' '*(length-1)+'|')

    for i in range(length):
        print('_', end = '')

    return
