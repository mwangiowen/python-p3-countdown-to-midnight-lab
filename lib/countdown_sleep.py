import time

def countdown_with_sleep(seconds):
    while seconds > 0:
        print(f'{seconds} SECOND(S)!')
        time.sleep(1)  
        seconds -= 1
    print('HAPPY NEW YEAR!')

print(countdown_with_sleep(10))