# Capturing the images to create the Labels

import cv2
import os
import time
import uuid

# Image path
path = os.getcwd()
IMAGES_PATH = (
    f"{os.path.abspath(os.path.join(path, os.pardir))}/data/images/colletedimages"
)
print(IMAGES_PATH)

# Label --> comes from the user in future
labels = ["hello", "thanks", "yes", "no", "iloveyou"]
number_img = 15

# Creating the labels
for label in labels:
    os.mkdir(IMAGES_PATH + "/" + label)
    cap = cv2.VideoCapture(0)
    print(f"Collecting images for {label}")
    time.sleep(5)
    image_captures = 0
    for images in range(number_img):
        image_captures += 1
        print(f"starting image number:{image_captures} Capture")
        ret, frame = cap.read()
        image_name = os.path.join(
            IMAGES_PATH, label, f"{label}-{str(uuid.uuid1())}.jpg"
        )
        cv2.imwrite(image_name, frame)
        cv2.imshow("frame", frame)
        time.sleep(3)
        print(f"image {image_captures} captured")

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
