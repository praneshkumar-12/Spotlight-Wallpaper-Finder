import shutil
import os
from pathlib import Path
from time import sleep

os.system('pip install pillow')

import PIL
from PIL import Image

sleep(3)

user = os.getlogin()

src = 'C:/Users/' + user + '/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'
des = 'C:/Users/' + user + '/Pictures'

try:
    test = os.listdir(des)
    del test
except FileNotFoundError:
    des = 'C:/Users/' + user + '/OneDrive/Pictures'

new_folder_path = des + '/temp/'
files = os.listdir(src)
try:
    os.mkdir(new_folder_path)
except FileExistsError:
    pass

for i in files:
    shutil.copy2(os.path.join(src,i), new_folder_path)

for j in os.listdir(new_folder_path):
    source = new_folder_path + j
    target = new_folder_path + j + ".jpg"
    os.rename(source, target)

name_lst = []
for k in os.listdir(new_folder_path):
    img = PIL.Image.open(new_folder_path + k)
    wid, hgt = img.size
    if wid == 1920 and hgt == 1080:
        name_lst.append(new_folder_path + k)
    img.close()

for l in name_lst:
    shutil.copy2(l, des)

print(f"Files Moved: {len(name_lst)}")

file_paths = []
for each_image in os.listdir(new_folder_path):
    file_path = os.path.join(new_folder_path, each_image)
    file_paths.append(file_path)

for elt in file_paths:
    os.remove(elt)

print("Removal Done")

print("This window will be closed in 7 seconds...")
sleep(7)
 