import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 불러오는 함수 정의
def load_image(file_path):
    image = cv.imread(file_path)
    if image is None:
        raise FileNotFoundError(f"Unable to find or open the file: {file_path}")
    return image

# 각 이미지를 개별적으로 불러옴
img1 = load_image('001.jpg')
img2 = load_image('002.jpg')
img3 = load_image('003.jpg')

# 이미지들을 리스트에 추가
images = [img1, img2, img3]

# OpenCV의 createStitcher 함수를 이용해 이미지들을 스티칭
stitcher = cv.Stitcher.create()
status, stitched_image = stitcher.stitch(images)

# 스티칭이 성공했으면 결과 이미지를 저장하고 표시함
if status == cv.Stitcher_OK:
    # 이미지를 저장한다
    stitched_image_path = 'stitched_image.jpg'
    cv.imwrite(stitched_image_path, stitched_image)

    # 스티칭된 이미지를 불러옴
    stitched_image = cv.imread(stitched_image_path)

    # OpenCV는 BGR 색상 체계를 사용하니까, 이미지를 RGB로 변환
    stitched_image_rgb = cv.cvtColor(stitched_image, cv.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))
    plt.imshow(stitched_image_rgb)
    plt.axis('off') 
    plt.show()
else:
    print("Image stitching failed with error code:", status)
