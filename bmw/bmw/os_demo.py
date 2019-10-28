import os

images_path = os.path.join(str(os.path.dirname(os.path.abspath(__file__))), 'images')
if not os.path.exists(images_path):
    os.mkdir('images')
else:
    print('文件已经存在！')


