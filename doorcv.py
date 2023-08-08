## 현재 상황 : canny filter로 edge detection을 하는 값까지는 최적화 했는데, contour를 그리면 다른 물체들도 같이 그려짐 + 윤곽 제대로 안잡힘

import cv2
import numpy as np


img = cv2.imread('./Photos/door.jpg')

# 흑백
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 노이즈 제거
img = cv2.GaussianBlur(img, (5, 5), 0)

# canny filter 임계값 설정
lower = 171
upper = 250

# threshold 임계값 설정 
# 경험적으로 제일 괜찮았던 값임
low_thresh = 127
high_thresh = 255

while True:
    imgcopy = img.copy()
    
    # canny filter로 edge detection
    edges = cv2.Canny(imgcopy, lower, upper)

    # cv2.imshow("Edges",edges)
    # find contours
    # adjust threshold value to get more or less contours
    # ret, thresh = cv2.threshold(imgcopy, low_thresh, high_thresh, 0)
    contours, hierarchy = cv2.findContours(imgcopy, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # contour 그리기
    cv2.drawContours(imgcopy, contours, -1, (0, 255, 0), 3)

    # 출력
    cv2.imshow('image', imgcopy)
    cv2.waitKey(1)

    continueOrNot = input("Continue? : ")
    if continueOrNot == "":
        pass
    else:
        exit()
    # low_thresh = int(input("Lower : "))
    # high_thresh = int(input("Upper : "))
    # print()
    cv2.destroyAllWindows()
    
    # # cv2.imshow('image', img)