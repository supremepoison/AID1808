f = open('mynote.txt', 'rb')
b = f.read()
print("The length is :", len(b))

print('content:',b)
s = b.decode()
print("transfer to string:",s)
f.close
