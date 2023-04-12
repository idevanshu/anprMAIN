import cv2
import os
import easyocr
import csv
import pyautogui
import imgenhancer
import time
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
visited = []
with open("plates.csv" , "r") as f:
    red= csv.reader(f)
    for lines in red:
        visited.append(lines[0])

frameWidth = 640
franeHeight = 480
plateCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
minArea = 100
reader = easyocr.Reader(['en'])
cap = cv2.VideoCapture("C:/Users/ASUS/Downloads/Video/Pexels Videos 2103099.mp4")
cap.set(3, frameWidth)
cap.set(4, franeHeight)
cap.set(10, 150)

# mp4_files = [filename for filename in os.listdir(os.getcwd()) if filename.endswith('.mp4')]
# count_mp4_files = len(mp4_files)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(f'Video-{count_mp4_files}.mp4', fourcc, 30.0, (frameWidth, franeHeight))

count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = plateCascade.detectMultiScale(imgGray, scaleFactor=1.05, minNeighbors=5)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            imgRoi = img[y:y + h, x:x + w]
            result = reader.readtext(imgRoi)
            if result:
                plateNumber = result[0][1]
                
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)

    # out.write(img)
    plateNumber = "".join(plateNumber).upper()
    print(plateNumber)
    if plateNumber == visited[0]:
        print("Vehicle detected")
        # ss
        cv2.imwrite(f"numplate_img/img{count}.png",img)
        break

    if cv2.waitKey(1) & 0xFF == ord('s'):
        if result:
            cv2.imwrite(os.getcwd() + "\\" + str(count) + ".jpg", imgRoi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Scan Saved", (15, 265), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
            count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

parameters = {}
parameters['local_contrast'] = 1.5  # 1.5x increase in details
parameters['mid_tones'] = 0.5
parameters['tonal_width'] = 0.5
parameters['areas_dark'] = 0.7  # 70% improvement in dark areas
parameters['areas_bright'] = 0.5  # 50% improvement in bright areas
parameters['saturation_degree'] = 1.2  # 1.2x increase in color saturation
parameters['brightness'] = 0.1  # slight increase in brightness
parameters['preserve_tones'] = True
parameters['color_correction'] = False

img_data = Image.open("numplate_img/img0.png")
numpydata = np.asarray(img_data)
enhanced_img = imgenhancer.enhance_image(numpydata , parameters)

plt.imshow(enhanced_img)
plt.title('Enhanced image')
plt.axis('off')
plt.tight_layout()

plt.show()
cap.release()
# out.release()
cv2.destroyAllWindows()