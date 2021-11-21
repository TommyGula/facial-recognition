# facial-recognition
Connect WebCam, save face's photos and then predict with a Neural Network!
I tried not to use "facial_recognition" package because I wanted to build the model on my own

*How to use it?*

1) Type python camera.py -l (your label name)

ARGUMENTS:

-l : LABEL --> This is a required arg. It's also the folder name where following images will be saved

2) Type python train_model.py: the model will be trained with the images previously taken

3) Type python facial_recognition.py: It will open your webcam, and it will show the labeled prediction once it is recognised
