
import cv2 as cv
import numpy as np

net = cv.dnn.readNet('../darknet/yolov3.weights', '../darknet/cfg/yolov3.cfg')

classes = []

with open('../darknet/data/coco.names', 'r') as f:
    classes =  f.read().splitlines()

#print(classes)
img = cv.imread('../darknet/data/dog.jpg')

height, width , a = img.shape
print(f'{height}, {width}')

blob = cv.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)

'''
for b in blob:
    for n, img_blob in enumerate(b):
        cv.imshow(str(n), img_blob)
'''

net.setInput(blob)
output_layers_names = net.getUnconnectedOutLayersNames()
layerOutputs = net.forward(output_layers_names)

bouding_boxes = []
confidences = []
class_ids = []

for output in layerOutputs:
    print(output.shape)
    for detection in output:
        scores = detection[5:]
        #print(scores.shape)
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)
            w = int(detection[2]*width)
            h = int(detection[3]*height)

            x = int(center_x - w/2)
            y = int(center_y - h/2)

            bouding_boxes.append([x, y, w, h])
            confidences.append(confidence)
            class_ids.append(class_id)
        #print(detection)
print(len(bouding_boxes))

indexes = cv.dnn.NMSBoxes(bouding_boxes, confidences, 0.5, 0.4)
print(type(indexes))
print(indexes.flatten())

font = cv.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(bouding_boxes),3))

for i in indexes.flatten():
    x, y , w, h = bouding_boxes[i]
    label = str(classes[class_ids[i]])
    confidence = str(round(confidences[i], 2))
    color= colors[i]
    cv.rectangle(img, (x, y),(x+w, y+h), color, 2)
    cv.putText(img, label + " " + confidence,(x, y+20), font, 2, (255,255,255), 2 )

cv.imshow('Image', img)
cv.waitKey(0)