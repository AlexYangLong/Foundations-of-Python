from PIL import Image

# 打开图片资源
img = Image.open('hy.jpg')

# print(img)
# print(img.mode, img.size)

# 缩略图片
# img.thumbnail((200, 200))
#
# # 将缩略图片保存
# img.save('xhy.jpg', 'JPEG')

# 重置图片大小并保存
resizedIm = img.resize((1000, 1000))
resizedIm.save(r'resize.jpg')