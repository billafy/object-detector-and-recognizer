import cv2

class ObjectRecognizer : 
    def __init__(self, thresh=0.5, show_conf=True) : 
        self.configPath = './data/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        self.weightsPath = './data/frozen_inference_graph.pb'
        self.thresh = thresh
        self.show_conf = show_conf
        self.net = cv2.dnn_DetectionModel(self.weightsPath, self.configPath)
        self.net.setInputSize(320, 320)
        self.net.setInputScale(1.0/127.5)
        self.net.setInputMean((127.5, 127.5, 127.5))
        self.net.setInputSwapRB(True)
        with open('./data/coco.names', 'rt') as file : 
            self.classNames = file.read().rstrip('\n').split('\n')

    def recognize(self, frame) : 
        objects = dict()
        class_ids, confs, bbox = self.net.detect(frame, confThreshold=self.thresh)

        if len(class_ids) != 0 : 
            for class_id, conf, box in zip(class_ids.flatten(), confs.flatten(), bbox) : 
                class_name = self.classNames[class_id - 1].capitalize()
                if class_name in objects : 
                    objects[class_name]['count'] += 1
                    objects[class_name]['confidence'] = (objects[class_name]['confidence'] + conf) / 2
                else : 
                    objects[class_name] = {'name': class_name, 'count': 1, 'confidence': conf}
                cv2.rectangle(frame, box, (0, 255, 0), 1)
                cv2.putText(
                    frame, 
                    class_name, 
                    (box[0] + 10, box[1] + 30),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (0, 255, 0),
                    1
                )
                if self.show_conf : 
                    cv2.putText(
                        frame, 
                        str(round(conf*100, 2)),
                        (box[0]+200, box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (0, 255, 0),
                        1
                    )

        return frame, list(objects.values())