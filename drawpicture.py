from PIL import Image, ImageDraw, ImageFont
import os
import shutil

def drawimage(link, i):
    image = Image.open(link).convert("RGB")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except OSError:
        font = ImageFont.load_default()

    draw.text((100, 100), str(i), font=font, fill="black")

    image.save(f"anh_moi_{i}.png")
    image.show()
    output_folder = r"C:\Users\DELL\OneDrive\Desktop\sắp xếp tài liệu"
    os.makedirs(output_folder, exist_ok=True)
    shutil.copy(f"anh_moi_{i}.png", output_folder)