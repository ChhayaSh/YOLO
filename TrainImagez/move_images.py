import os

folders = ['cycle', 'BeautifulBusesYo']
path = r'C:\Users\chhav\Desktop\YOLOv3-Series-master\[part 4]OpenLabelling\images'


n=0
for folder in folders:
    for image in os.scandir(folder):
        n+=1
        os.rename(image.path, os.path.join(path,'{:06}.jpg'.format(n)))
