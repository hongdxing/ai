
import cv2

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print('webcam failed')

while True:
    # Capture the video frame
    # by frame
    ret, frame = capture.read()

    if ret:
        # Display the resulting frame
        cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

