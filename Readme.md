# The Running plates project(Machine learning) 
Read  bunch numbers from the runner plate![BIB OCR](https://www.thephuketnews.com/photo/listing/2016/1465177820_1-org.jpg)

## Getting Started

First of all, we need some prerequisites before we can run these project.

### Prerequisites
Tesseract OCR [here](https://github.com/tesseract-ocr/tesseract)
 - Tesseract 4.x   (my local is "tesseract 4.1.1")
 - eng.traineddata (model for tesseract)
```
$ tesseract --version
tesseract 4.1.1
 leptonica-1.75.3
  libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.2) : libpng 1.6.34 : libtiff 4.0.9 : zlib 1.2.11 : libwebp 0.6.1 : libopenjp2 2.3.0

 Found AVX2
 Found AVX
 Found FMA
 Found SSE
```
Python Packages

 - **pytesseract**
 - opencv(cv2)
 - PIL or Pillow
 - numpy

## Run

Run only **main.py**

```
python main.py
```

