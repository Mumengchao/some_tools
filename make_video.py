
import cv2

def make_video(outvid, images=None, fps=30, size=None,
               is_color=True, format='MPEG'):
    from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
    # fourcc = VideoWriter_fourcc(*format)
    vid = None
    for image in images:
        if not os.path.exists(image):
            raise FileNotFoundError(image)
        img = imread(image)
        if vid is None:
            if size is None:
                size = img.shape[1], img.shape[0]
            vid = VideoWriter(outvid, VideoWriter_fourcc(*format), float(fps), size, is_color)
        if size[0] != img.shape[1] and size[1] != img.shape[0]:
            img = resize(img, size)
        vid.write(img)
    vid.release()
    return vid

import glob
import os

# Directory of images to run detection on
IMAGE_DIR=('/home/cxz/projects/yolov3/img_res_10/')
VIDEO_DIR = ('/home/cxz/projects/yolov3/')
images = list(glob.iglob(os.path.join(IMAGE_DIR, '*.*')))
print(images)
# Sort the images by integer index
images = sorted(images)#, key=lambda x: float(os.path.split(x)[1][:-3]))
print(images)
outvid = os.path.join(VIDEO_DIR, "img_res_10.avi")
print(outvid)
make_video(outvid, images, fps=30)
