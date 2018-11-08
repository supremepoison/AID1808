# file : mypack/games/cotra.py

def play():
    print("正在玩 魂斗罗")
def game_over():
    # #绝对导入
    # from mypack.menu import show_menu
    # show_menu()
    #相对导入:相对于当前 mypack/games/
    from ..menu import show_menu
    show_menu()
    #调用mypack/games/tanks.py里的play()
    ...#相对导入
    from .tanks import play
    play()

print("魂斗罗模块被加载")
