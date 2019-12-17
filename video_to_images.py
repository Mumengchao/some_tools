import cv2
import time
import numpy as np


def video_to_images(video_path, img_path, n):
    cap = cv2.VideoCapture(video_path)
    i = 0
    while (True):
        ret, frame = cap.read()
        if ret:
            if i % n == 0:
                cv2.imwrite("{}{}{:07}{}".format(
                    img_path, '201912121606443_', i, '.jpg'), frame)  # 精确到毫秒
        else:
            break
        i += 1
        print(i)

    cap.release()


if __name__ == "__main__":
    video_path = "/home/cxz/datasets/qingdao_data/20191212加油站视频/1212试点加油站/静态静电识别/静电标志立体状态/192.168.1.2-001-201912121606443.mp4"
    image_path = "/home/cxz/datasets/qingdao_data/20191212加油站视频/1212试点加油站/静态静电识别/静电标志立体状态/images/"
    video_to_images(video_path, image_path, 2)
