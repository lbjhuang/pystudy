from PIL import Image, ImageFilter


#例子来源 https://blog.csdn.net/gzlaiyonghao/article/details/1852726
#打开一个图像
im = Image.open('./images/james.jpg')

#展示图片
im.show()
print(im.histogram())
#旋转图片并展示
im.rotate(45).show()

#获得图像尺寸
w , h = im.size
print('图像的宽度和高度是:%s,%s' % (w, h))

#缩略图
im.thumbnail((w//2, h//2))
im.save('./images/thumb.jpg', 'jpeg')

#模糊
im2 = im.filter(ImageFilter.BLUR)
im2.save('./images/blur.jpg', 'jpeg')
