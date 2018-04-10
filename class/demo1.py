class Student(object):
    def __init__(self, name, score):
        self.__name = name #定义私有属性(不加__就不是私有的了)
        self.__score = score

    def get_score(self):
        print('%s\'s score is %s' % (self.__name, self.__score))

    def __del__(self):
        print('析构方法，实例化后自动执行')


paul = Student('paul', 99)
#print(paul.name)  #无法获取类的私有属性，只能通过公有方法获取
paul.get_score()
paul.hobby = 'basketball'
print(paul.hobby)
print(isinstance(paul, Student))  #是否是Student实例
print(dir(paul))
