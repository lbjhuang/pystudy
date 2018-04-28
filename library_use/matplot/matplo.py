import matplotlib.pyplot as plt
import numpy as np


# 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 1, 50)
print(x)
#设置一个函数y
#y = 2*x*x + 1
y = 2**x + 1  #2的x次方+1

# 第一个是横坐标的值，第二个是纵坐标的值
plt.plot(x, y)
#设置轴标签
plt.xlabel('I am X')
plt.ylabel('I am Y')
# 必要方法，用于将设置好的figure对象显示出来
plt.show()