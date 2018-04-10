print('The quick brown fox' , 'jumps over' , 'the lazy dog')

# name = input('please enter your name') #接受输入内容传给一个变量name
# print('hello',name) #打印出输入的变量
print('I\'m back') #转移字符\
print(r"\\\t\'")  #r默认不转义
print(10/3) #除法,返回浮点数
print(10//3) #地板除法,取整数部分
print(len('很黄很暴力jkl')) #统计字符串字符个数---8

###格式化输出小案例
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
# 并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
r = (85-72)/72
print('%.1f' % (r*100),'%')