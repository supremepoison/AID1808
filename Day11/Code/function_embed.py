



def fn_outter():
    print("fn_outter被调用")

    def fn_inner(): 
        print("fn_inner被调用")

    fn_inner()      #第一次调用
    fn_inner()      #第二次调用
    print('fn_outter()调用结束')
    return fn_inner()

f = fn_outter()
#fn_inner()  #不可用
f  # fn_inner 被调用