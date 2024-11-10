import os
from PIL import Image
import pyocr.builders

#１．インストール済みのTesseractのお明日を通す
path_tesseract = r"C:\Program Files\Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract
#２．OCRエンジン取得
tools = pyocr.get_available_tools()
tool = tools[0]
#３．原稿画像の読み込み
img_org = Image.open("test1.png")
#４，OCR実行
builder = pyocr.builders.TextBuilder()
result = tool.image_to_string(img_org, lang="jpn", builder=builder)
print(result)
