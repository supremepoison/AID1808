def test(a,b,*args, c, **kwargs):
    print(a, b, args, c, kwargs)

test(1, 2, 3, 4, 5,(1,2,3),[123],{'d':2}, c =[311], d = {'d':15})