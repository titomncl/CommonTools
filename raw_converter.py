# from PIL import Image
# import exifread as exif
import rawpy
import imageio
import os
from concat import concat
import tkinter as tk
from tkinter import filedialog



def _del_backslash(text):
    return text.replace('\\', '/')

if __name__ == '__main__':

    root = tk.Tk()
    root.withdraw()

    path = filedialog.askdirectory(initialdir="E:/00_DRIVE/LUMIX")

    files_to_convert = list()

    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith((".RW2", ".rw2")):
                files_to_convert.append(concat(_del_backslash(root), name, separator="/"))

    path = files_to_convert[-1].rsplit("/", 1)[0]
    jpg_path = path.replace("RAW", "JPG")

    try:
        os.mkdir(jpg_path)
    except FileExistsError:
        pass

    if files_to_convert is not None:
        for file in files_to_convert:
            # file = file.name
            raw_path, raw_file = os.path.split(file)
            raw_path_file = concat(raw_path, raw_file, separator="/")

            jpg_file = raw_file.replace("RW2", "jpg")
            jpg_out = concat(jpg_path, jpg_file, separator="/")

            with rawpy.imread(raw_path_file) as raw:
                # raises rawpy.LibRawNoThumbnailError if thumbnail missing
                # raises rawpy.LibRawUnsupportedThumbnailError if unsupported format
                thumb = raw.extract_thumb()
            if thumb.format == rawpy.ThumbFormat.JPEG:
                # thumb.data is already in JPEG format, save as-is
                print(jpg_out)
                with open(jpg_out, 'wb') as f:
                    f.write(thumb.data)
            elif thumb.format == rawpy.ThumbFormat.BITMAP:
                # thumb.data is an RGB numpy array, convert with imageio
                imageio.imsave(jpg_out, thumb.data)


    # img_data = open(file, 'rb')
    #
    # tags = exif.process_file(img_data)
    #
    # img_width = int(str(tags["Image Tag 0x0002"]))
    # img_length = int(str(tags["Image Tag 0x0003"]))
    #
    # raw_data = open(file, "rb").read()
    #
    # # Use the PIL raw decoder to read the data.
    # # the 'F;16' informs the raw decoder that we are reading
    # # a little endian, unsigned integer 16 bit data.
    # img_size = (img_width, img_length)
    #
    # img = Image.frombytes('L', img_size, raw_data, 'raw', 'F;16')
    # img.save("C:/Users/t.nicole/Desktop/foo.png")



