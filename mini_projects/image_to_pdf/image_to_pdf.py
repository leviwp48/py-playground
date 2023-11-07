import sys
import img2pdf
import os

filepath = sys.argv[1]
if os.path.isfile(filepath):
    if filepath.endswith(".jpg"):
        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(filepath))
elif os.path.isdir(filepath):
    with open("output.pdf", "wb") as f:
        imgs = []
        for filename in os.listdir(filepath):
            if not filename.endswith(".jpg"):
                continue
            path = os.path.join(filepath, filename)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        f.write(img2pdf.convert(imgs))
else:
    print("please input file or dir")