#  有一个bytearray 字节数组
#         ba = bytearray(b'a1b2c3d4')
#         如何得到字节串'1234'和'abcd'
#         将上述字节数组改为:
#         ba = bytearray(b'A1B2C3D4')


ba = bytearray(b'a1b2c3d4')
print(ba[::2])
print(ba[1::2])
c = 0
for i in range(0,len(ba),2):
    ba[i] =  65+c
    c+=1

# ba = bytearray(b'A1B2C3D4')
print(ba)
