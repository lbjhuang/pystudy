import matplotlib.pyplot as plt
import numpy as np


# 当我们需要在画板中绘制两条线的时候，可以使用下面的方法：
# 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 1, 50)
print(x)
y = 2*x + 1
z = 2**x + 1  #2的x次方+1

# 第一个参数表示的是编号，第二个表示的是图表的长宽
plt.figure(num = 3, figsize = (8,5))

#设置轴标签
plt.xlabel('I am X')
plt.ylabel('I am Y')

#设置取值范围
plt.xlim((-1, 2))
plt.ylim((1, 3))

# 设置坐标轴一些位置和提示： 第一个参数是点的位置，第二个参数是点的文字提示。
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
          ['really bad', 'bad', 'normal', 'good', 'readly good'])

ax = plt.gca()
# 将右边和上边的边框（脊线）的颜色去掉
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 绑定x轴和y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 定义x轴和y轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

#绘制曲线并设置样式
plt.plot(x, z)
plt.plot(x, y, color = 'red', linewidth = 1.1, linestyle = '--')
# 必要方法，用于将设置好的figure对象显示出来
plt.show()