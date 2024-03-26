import cv2


def extract_video_frame(video_path):
    if video_path is None:
        return []

    cap = cv2.VideoCapture(video_path)

    frames = []

    while cap.isOpened():
        ret, frame = cap.read()

        if ret is False:
            break

        frames.append(frame)

    cap.release()
    return frames


if __name__ == "__main__":
    cap = cv2.VideoCapture("toothlessdancing_shorts.mp4")
    # cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret is False:
            break
    cap.release()
    cv2.destroyAllWindows()
