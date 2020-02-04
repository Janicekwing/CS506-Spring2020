def draw_hospital(length=20):
    """
        Argument length is the width of the building
        Returns an image of a hospital building using keyboard characters
    """

    for i in range(length):
        print('_', end = '')

    print('\n|'+' '*((length-len('hospital'))//2), end = '')
    print('HOSPITAL',end='')
    print(' '*((length-len('hospital'))//2)+'|\n', end = '')

    for i in range(length):
        print('_', end = '')

    for i in range(5):
        print('|'+' '*(length-1)+'|')

    for i in range(length):
        print('_', end = '')

    return
