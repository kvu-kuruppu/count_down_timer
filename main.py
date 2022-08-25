import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        # print(f'\r{timer}', end='')
        time.sleep(1)
        t -= 1

    print('Time is up!')

t = input('Input time in seconds: ')

countdown(int(t))


