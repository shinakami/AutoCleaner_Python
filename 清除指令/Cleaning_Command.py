import time 
import os



def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print('Time: ', min_sec_format, end='\n')
        time.sleep(1)
        num_of_secs -= 1
        

    print('Countdown finished.')




if __name__ == '__main__':

    print(time.ctime())
    time.sleep(10)

    duration = 2400

    while(True):
        os.system("cls")
        os.system("C:/Users/User/Desktop/清除指令/PYKAMIA的清除系統資料.bat")
        countdown(duration)

