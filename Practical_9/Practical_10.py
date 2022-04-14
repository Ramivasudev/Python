# D21CS104
# Rami Vasudev
# importing necessary libraries
import img2pdf
from PIL import Image
import os

import img2pdf

with open("D:/converted_img.pdf",'wb') as f:
    f.write(img2pdf.convert('D:/img.jpg'))
# output
print("Successfully made pdf file")
