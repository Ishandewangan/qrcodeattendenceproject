import cv2
import datetime
import qrcodedatabase as qrd

def read_attendence():
    cap = cv2.VideoCapture(0+0 + cv2.CAP_DSHOW)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if bbox is not None:
            bb_pts = bbox.astype(int).reshape(-1, 2)
            num_bb_pts = len(bb_pts)
            for i in range(num_bb_pts):
                cv2.line(img,
                     tuple(bb_pts[i]),
                     tuple(bb_pts[(i+1) % num_bb_pts]),
                     color=(255, 0, 255), thickness=2)
            if data:
                a=data[1:4]
                b=datetime.date.today()
                qrd.dataVerify(a,b)
        cv2.imshow("img", img)    
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
