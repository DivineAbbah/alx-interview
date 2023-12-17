#!/usr/bin/python3
''' minimum operations challenge.
'''


def minOperations(n):
    '''inputs fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    op_count = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            op_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            op_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            done += clipboard
            op_count += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return op_count
