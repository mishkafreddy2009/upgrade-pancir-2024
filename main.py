from ultralytics import YOLO
import GPUtil
import cvzone
import cv2
import math
import time
import psutil
import argparse

import config


FRAME_SIZE = (1280, 720)
FONT = cv2.FONT_HERSHEY_PLAIN
FONT_BIGGER = cv2.FONT_HERSHEY_SIMPLEX


def get_parsed_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=False,
                    help="path to model")
    ap.add_argument("-v", "--video", required=False,
                    help="path to input .mp4 file")
    args = vars(ap.parse_args())
    return args


def draw_boxes(result, frame, classnames: list) -> None:
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            classname = int(box.cls[0])
            if confidence > 10:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame,(x1, y1),(x2, y2), (0, 0, 255), 2)
                cvzone.putTextRect(frame, f"{classnames[classname].upper()} {confidence}%",
                                   [x1, y1],
                                   scale=2, thickness=2, font=FONT)


def calculate_fps(start_time: float) -> float:
    end_time = time.time()
    fps = math.ceil(1 / (end_time - start_time))

    return fps


def show_info(frame, info_title: str, info, x: int, y: int, font=FONT) -> None:
    cv2.putText(frame, f"{info_title} {info}", (x, y), font, 3, (100, 255, 0), 2, cv2.LINE_AA)


def main():
    nvidia_gpus = GPUtil.getAvailable() # check for available nvidia gpus

    args = get_parsed_args()

    model = YOLO(config.main_model) # set default yolo model
    classnames = ["Fire", "Smoke"]
    cap = cv2.VideoCapture(config.video) # set default testing video

    if args["model"]:
        model = YOLO(args["model"])
    if args["video"]:
        cap = cv2.VideoCapture(args["video"])

    while (cap.isOpened()):
        start_time = time.time()

        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, FRAME_SIZE)
        result = model(frame, stream=True)

        draw_boxes(result, frame, classnames)

        if nvidia_gpus:
            gpu_usage = GPUtil.showUtilization(attrList="memoryUsed")
            show_info(frame, "GPU", gpu_usage, 0, 50)

        fps = calculate_fps(start_time)
        cpu_usage = f"{psutil.cpu_percent()}%"
        ram_usage = f"{psutil.virtual_memory().percent}%"

        show_info(frame, "FPS", fps, 0, 100)
        show_info(frame, "CPU", cpu_usage, 0, 150)
        show_info(frame, "RAM", ram_usage, 0, 200)

        cv2.imshow("firesmoke detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"): 
            break

    cap.release()


if __name__ == "__main__":
    main()
    cv2.destroyAllWindows()
