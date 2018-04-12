class Student(object):
    def __init__(self, name, score):
        self.name = name #定义私有属性(不加__就不是私有的了)
        self.score = score

    def get_score(self):
        print('%s\'s score is %s' % (self.name, self.score))


    def eat(self, food):
        print('%s is eating %s' % (self.name, food))

paul = Student('paul', 99)

func = input("请输入要调用的方法：")
if hasattr(paul, func):
    do = getattr(paul, func)
    do('banana')

# 通过字符串调用和操作方法或者属性即为反射
# 其实，反射就是通过字符串的形式，导入模块；通过字符串的形式，去模块寻找指定函数，并执行。
# 利用字符串的形式去对象（模块）中操作（查找/获取/删除/添加）成员，一种基于字符串的事件驱动！