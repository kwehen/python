from PIL import Image
import numpy as np
import pytesseract
from pdf2image import convert_from_path, convert_from_bytes

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
poppler_path = r"C:/Users/is00kxh/Downloads/Poppler/poppler-23.07.0/Library/bin"

pages = convert_from_bytes(open("C:/Users/is00kxh/Downloads/Course Kick Start_D332.pdf", "rb").read(), poppler_path=poppler_path)

for i, page in enumerate(pages):
    fname = "image"+str(i)+'.png'
    page.save(fname, "PNG")


images_from_path = ["image0.png", "image1.png", "image2.png"]

for image in images_from_path:
    img = Image.open(image)
    text = pytesseract.image_to_string(img)
    new_file = open("Test-text.txt", "a")
    new_file.write(text)