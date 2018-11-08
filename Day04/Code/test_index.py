s = input('input:')
l = len(s)
print(s, "length：", l)
print("first:",s[0])
print('last:',s[l-1])
if l%2 != 0 :
    print("odd")
    print("center:", s[l//2])
else:
    print("even")