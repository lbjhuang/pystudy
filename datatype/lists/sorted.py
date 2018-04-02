#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：

list = [36,12,-8,15,2,6]

ls = sorted(list, key=abs)
print(ls)

#按照大小写字母的排序
list2= ['paul', 'sam', 'tim', 'bob']
ls2 = sorted(list2, key=str.lower)    #正向顺序排序
ls3 = sorted(list2, key=str.lower, reverse=True) #还可以翻转排序
print(ls3)
#从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。

student = [{"name":"huang","age":18,"hobby":"basketball"},
           {"name":"wei","age":19,"hobby":"football"},
           {"name":"liu","age":20,"hobby":"art"}]

#根据某个字段的顺序来排序 的方法：  lambda表达式
#student.sort(key=lambda x:x.get('name'))  # name: huang liu wei
student.sort(key=lambda x:x['name'])
#new_student = sorted(student, key=lambda x:x['hobby'])  #根据某个字段的顺序来排序 hobby:  liu huang wei
new_student = sorted(student, key=lambda x:x.get('hobby'))  #根据某个字段的顺序来排序 hobby:  liu huang wei
print(new_student)
