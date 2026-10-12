#Ghi ảnh theo số thứ tự
from paddleocr import PaddleOCR
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from drawpicture import drawimage
import os
import shutil
from paddleocr import PaddleOCR

ocr = PaddleOCR(
    lang="vi",
    device="cpu",
    enable_mkldnn=False
)

def readpictures(link):

   ocr = PaddleOCR(lang="vi")
   result = ocr.predict(link)
   output_folder=r"C:\Users\DELL\OneDrive\Desktop\sắp xếp tài liệu"
   os.makedirs(output_folder, exist_ok=True)

   doc = []

   data=pd.read_excel(r"C:\Users\DELL\Downloads\CV.xlsx")
   data.columns = data.columns.astype(str).str.strip()

   for res in result:
      df = res.json
      doc.extend(df["res"]["rec_texts"])


   for index,i in data["sdt"].items():
      if str(i) in doc:
         drawimage(link,index+1)