

# 0x00 0x01 0x02... 0xFF # 256


try:
    f = open('0_255.bin', 'wb')     # binary write
    b = bytes(range(256))
    f.write(b)

    f.close()
    print("input data successfully")
except OSError:
    print("input data failed")