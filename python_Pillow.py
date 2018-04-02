# Pillow 事实上已经是一个Python的图像处理标准库了
from PIL import Image, ImageFilter  # 操作图像
im = Image.open('/home/nifer/Pictures/Wallpapers/tt.jpg')
w, h = im.size
print('图像的大小为：', im.size, '图像的格式：', im.format, '图像的模式:', im.mode)  # 图像的相关信息
im.thumbnail((w // 2, h // 2))  # 缩放50%
print('缩放后的大小为:', im.size)
im.save('thumbnail.jpg', 'jpeg')  # 把缩放后的图像用jpeg格式保存:

# 图像模糊效果
im = im.filter(ImageFilter.BLUR)
im.save('blur.jpg', 'jpeg')
