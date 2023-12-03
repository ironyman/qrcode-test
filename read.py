import cv2
# read the QRCODE image
img = cv2.imread("site.png")


# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox[0])
    print(f"bbox: {bbox} n_lines: {n_lines}")
    for i in range(n_lines):
        # draw all lines
        point1 = tuple([int(a) for a in bbox[0][i]])
        point2 = tuple([int(a) for a in bbox[0][(i+1) % n_lines]])
        print(point1, point2)
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

# display the result
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

