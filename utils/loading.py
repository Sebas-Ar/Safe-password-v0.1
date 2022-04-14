import time
import sys
import os

def loading(alert = '', text = 'loading', timeInterval = .2, size = 20):
    '''
    loading interface for show a message to users
    '''

    # show a message centrado
    print(f'\n\t\t{alert}\n')

    # Go through size of loading bar
    for s in range(size):
        # show pipe simbol n veces
        pipe = '|' * s
        # show line simbol n veces
        line = '-' * (size - s - 1)
        # write the loading bar
        sys.stdout.write(f'\r\t\t{text} [{pipe}{line}]')
        # rewrite text in before line
        sys.stdout.flush()
        # stop program
        time.sleep(timeInterval)

    # clean screen
    os.system('clear')
