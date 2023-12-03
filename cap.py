import cv2
# initalize the cam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    if bbox is not None:
        # print(f"QRCode data:\n{data}")
        # display the image with lines
        # length of bounding box
        n_lines = len(bbox[0])
        # print(f"bbox: {bbox} n_lines: {n_lines}")
        for i in range(n_lines):
            # draw all lines
            point1 = tuple([int(a) for a in bbox[0][i]])
            point2 = tuple([int(a) for a in bbox[0][(i+1) % n_lines]])
            # print(point1, point2)
            cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

    if data:
        print("[+] QR Code detected, data:", data)
    # display the result
    cv2.imshow("img", img)    
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

