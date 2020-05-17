import pytesseract
import os
from pre_processing import pre_image
import utilities as util


def main():
    path = 'images/'
    custom_config = r' -c tessedit_char_whitelist=0123456789 --psm 8'
    list_image = os.listdir(path)
    list_image.sort(key=lambda f: int(os.path.splitext(f)[0]))
    answer = []
    result = []

    for index, image in enumerate(list_image):
        img = pre_image(image)
        text = pytesseract.image_to_string(img, lang='eng', config=custom_config)
        result.append(text)
        print("Index %d: %s" % (index, text))
        index += 1

    print(util.percentage_corrected(result, answer))


# Driver code
if __name__ == '__main__':
    if util.is_rename():
        pass
    else:
        util.rename_image("images")

    main()
