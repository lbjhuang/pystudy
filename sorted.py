list = [36,12,-8,15,2,6]
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
ls = sorted(list, key=abs)
print(ls)

#按照大小写字母的排序
list2= ['paul', 'sam', 'tim', 'bob']
ls2 = sorted(list2, key=str.lower)    #正向顺序排序
ls3 = sorted(list2, key=str.lower, reverse=True) #还可以翻转排序
print(ls3)
#从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。
