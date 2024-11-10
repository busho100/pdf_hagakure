import streamlit as st
import os
import pyocr
import pyocr.builders
from PIL import Image

# １．インストール済みのTesseractのパスを通す
path_tesseract = r"C:\Program Files\Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract

# ２．OCRエンジン取得
tools = pyocr.get_available_tools()
tool = tools[0]

# Streamlit アプリのタイトル
st.title("画像リーダー")

# 画像ファイルのアップロード
upload_file = st.file_uploader("アップロード", type=["png", "jpg", "jpeg"])

if upload_file is not None:
    # アップロードされた画像をPILで開く
    upload_img = Image.open(upload_file)
    
    # 画像を表示
    st.image(upload_img, caption="アップロードされた画像", use_column_width=True)
    
    # OCR処理
    builder = pyocr.builders.TextBuilder()
    result = tool.image_to_string(upload_img, lang="jpn", builder=builder)
    
    # OCR結果を表示
    st.subheader("OCR結果")
    st.text(result)

    # OCR実行ボタンの作成
    if st.button("OCR実行"):
        # OCR処理
        builder = pyocr.builders.TextBuilder()
        result = tool.image_to_string(upload_img, lang="jpn", builder=builder)
        
        # OCR結果を表示
        st.subheader("OCR結果")
        st.text(result)
