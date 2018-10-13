import cv2
import time

# cv2.namedWindow("Preview")
# uncomment above line to the video. Three lines should be uncommented, including this.

start = time.time()

vc = cv2.VideoCapture(0)

out = cv2.VideoWriter('C:\\Users\\Asus\\Desktop\\output.avi', -1, 20.0, (640, 480))

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
t = 0
while t < 20 and rval:
    # cv2.imshow("Preview", frame)
    # uncomment above line to the video
    rval, frame = vc.read()
    out.write(frame)
    t = time.time() - start
    key = cv2.waitKey(20)
    if key == 27:
        break
out.release()
# cv2.destroyWindow("Preview")
# uncomment above line to the video