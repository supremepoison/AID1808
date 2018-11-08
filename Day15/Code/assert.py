
#此示例示意assert 语句的用法:

def get_score():
    s = int(input("Enter the score of student(0-100):"))
    assert 0 <= s <=100, "the score out of range"
    return s
try:
    score = get_score()
    print("The score is :", score)
except AssertionError as err:
    print("AssertionError 类型的错误:",err)