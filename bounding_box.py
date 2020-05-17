import cv2
import pytesseract

img = cv2.imread('./images/1.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

custom_config = r' --oem 3 --psm 6 outputbase digits'
#custom_config = r' -c tessedit_char_whitelist=0123456789 --oem 3 --psm 6'
hImg, wImg, = img.shape
print(img.shape)
boxes =  pytesseract.image_to_boxes(img, config=custom_config)
for b in boxes.splitlines():
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, 400+y), (w, h), (0, 0, 255), 2)
    cv2.putText(img, b[0], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyWindow()

