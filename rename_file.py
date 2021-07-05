import os

path = "E:/00_DRIVE/ISART_MFX1/DYNAMICS/NICOLE_Thomas/DYNAMICS_01/OUT/004"

path_content = os.listdir(path)

filename = "NICOLE_Thomas_test_004_"
ext = ".exr"

for i, item in enumerate(path_content):
    i += 1

    old_filepath = path + "/" + item
    new_filepath = path + "/" + filename + str(i).zfill(4) + ext

    os.rename(old_filepath, new_filepath)
