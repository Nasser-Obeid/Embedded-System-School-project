import cv2
import serial
from deepface import DeepFace
from serial.tools import list_ports
import os


def recognition(frame) -> str:
    if len(frame) > 0:
        cv2.imwrite('temp.jpg', frame)

        for i in os.listdir('faces'):
            if str(i)[-3:] == 'jpg':
                verification = DeepFace.verify(os.path.join('faces', i), img2_path='temp.jpg', enforce_detection=False,
                                               threshold=0.35)
                if verification["verified"]:
                    print("True")
                    try:
                        os.remove("temp.jpg")
                    except:
                        pass
                    return "A"
        print("False")
        try:
            os.remove("temp.jpg")
        except:
            pass
        return "B"
    print("No face detected.")
    return "C"


def create_user(face) -> None:
    if len(face) > 0:
        inp = input("Enter your username: ")
        cv2.imwrite(os.path.join('faces', f'{inp}.jpg'), face)


def main() -> None:
    cam = cv2.VideoCapture(0)

    ports = list_ports.comports()
    instance = serial.Serial()
    ports_list = []

    for port in ports:
        ports_list.append(port.device)

    print(ports_list)

    use = ""
    select = input('please enter the port of the arduino: COM')
    for i in ports_list:
        if i.startswith('COM' + select):
            use = 'COM' + select
            print("Using port:" + use)

    instance.baudrate = 9600
    instance.parity = 'N'
    instance.port = use
    instance.open()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        bbox = []
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            bbox = frame[y:y + h, x:x + w]

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            # break from the image capturing loop
            break

        if cv2.waitKey(1) & 0xFF == ord('n'):
            # to create new user
            create_user(bbox)

        if cv2.waitKey(1) & 0xFF == ord('r'):
            # to check if user is registered
            var = recognition(bbox).encode()
            instance.write(var)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
