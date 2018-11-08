#file:mypack/games/__init__.py
#此列表将在from mypack.games import * 时起作用,只导入 contra 和tanks模块
__all__ = ['contra', 'tanks']
print("mypack下的games子包被导入")
