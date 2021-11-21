# Opening webcam for screenshots

import cv2
from time import sleep
import os
import argparse

def open_and_screenshot(emotion, save_path):
    path = save_path + '/' + emotion

    # Hacer un filtro para que si ya existe la ruta que NO la cree!!!
    if os.path.isdir(path) == False:
        os.mkdir(save_path + '/' + emotion)

    n = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    print(n)

    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    sleep(2)
    while True:
        try:
            check, frame = webcam.read()
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 

                cv2.imwrite(os.path.join(path, str(n) + '.jpg'), img=frame)
                print("Processing image...")
                img_ = cv2.imread(os.path.join(path, str(n) + '.jpg'), cv2.IMREAD_ANYCOLOR)
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                img_ = cv2.resize(gray,(250,250))
                img_resized = cv2.imwrite(os.path.join(path, str(n) + '.jpg'), img=img_)
                print("Image saved!")
                n += 1

                #cv2.imwrite(os.path.join(path, str(n) + '.jpg'), img=frame)
                #print("Image saved!")
            
            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break
        
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Emotion Recognition")
    required_parser = parser.add_argument_group("required arguments")
    required_parser.add_argument('-label', '-l', help="Write the emotion you're gonna play for recognition dataset", required=True)
    args = parser.parse_args()

    save_path = 'C:/Users/tomii/Documents/Excersises/emotion_recognition/images'

    open_and_screenshot(args.label, save_path)