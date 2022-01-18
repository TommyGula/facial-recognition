# facial-recognition
Connect WebCam, save face's photos and then predict with a Neural Network!
I tried not to use "facial_recognition" package because I wanted to build the model on my own

*How to use it?*

1) Type python camera.py -l (your label name): This will open your webcam. By pressing "s" it will take a picture that will be saved for training. Press "q" to close the webcam.

    ARGUMENTS:

    -l : LABEL --> This is a required arg. It's also the folder name where following images will be saved

2) Type python train_model.py: the model will be trained with the images previously taken

3) Type python face_recognition.py: It will open your webcam, and it will show the labeled prediction once it is recognised
