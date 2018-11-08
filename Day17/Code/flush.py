import time

f = open('myflush.txt','w')
f.write('aaaaaaaa')
f.flush()   #强制清空缓冲区


while True:
    time.sleep(2)

f.close()