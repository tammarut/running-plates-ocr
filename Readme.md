# The Running Bib(Machine learning) 
Read  bunch numbers from the runner bib![BIB OCR](https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/AOZWACT3QJ3QH/5b658652-e819-487f-b7a5-d614cfa065f1._CR0,0,970,600_PT0_SX970__.jpg)

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
Take your **test-images** to directory ***images***

    images/your-test-images-directory

Run only **main.py**

```
python main.py
```

