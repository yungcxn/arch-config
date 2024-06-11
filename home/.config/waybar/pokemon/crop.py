import cv2
import os

for i in os.listdir():
  if i == "crop.py":
    continue
  im = cv2.imread(i, cv2.IMREAD_UNCHANGED)
  x, y, w, h = cv2.boundingRect(im[..., 3])
  im2 = im[y:y+h, x:x+w, :]
  cv2.imwrite(i, im2)