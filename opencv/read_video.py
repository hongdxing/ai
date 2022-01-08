
import cv2

capture = cv2.VideoCapture('./images/Cute Cat.mp4')
print(type(capture))

if not capture.isOpened():
    print("Error opening the video file")
else:
    fps = capture.get(5) # CAP_PROP_FPS
    print(f'Frames per second : {fps}')
    frame_count  = capture.get(7) # CAP_PROP_FRAME_COUNT
    print(f'Frames count: {frame_count}')

while capture.isOpened():
    result, frame = capture.read()
    if result:
        cv2.imshow('Cat',frame)
        key = cv2.waitKey(10)

        if key == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()

