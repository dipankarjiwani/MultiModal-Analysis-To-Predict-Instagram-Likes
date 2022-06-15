import os
import shutil

image_data = '.\image_data'
profiles = '.\profiles'

rows = []
rootdir = 'C:\\Users\\rachi\\OneDrive\\Desktop\\Sem 6\\ML\\Project\\image_data'

#iterate through images
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        original = os.path.join(subdir, file)
        # print(os.path.join(subdir, file))
        shutil.copy(original, rootdir)