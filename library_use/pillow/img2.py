from PIL import Image, ImageFilter

im = Image.open('./images/james.jpg')

#灰度图(多种模式1 L P RGB....)
#1 (1-bit pixels, black and white, stored with one pixel per byte)
#L (8-bit pixels, black and white)
#P (8-bit pixels, mapped to any other mode using a colour palette)
#RGB (3x8-bit pixels, true colour)
#RGBA (4x8-bit pixels, true colour with transparency mask)
#CMYK (4x8-bit pixels, colour separation)
#YCbCr (3x8-bit pixels, colour video format)
#I (32-bit signed integer pixels)
#F (32-bit floating point pixels)
im1 = im.convert('L')
im1.save('./images/huidu.jpg', 'jpeg')


rgb2xyz = (
    0.412453, 0.357580, 0.180423, 0,
    0.212671, 0.715160, 0.072169, 0,
    0.019334, 0.119193, 0.950227, 0 )
im2 = im.convert("RGB", rgb2xyz)
im2.save('rgb2xyz.jpg', 'jpeg')