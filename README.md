# FaceRec apply to Attendance Systems

A simple working facial recognition program.


## Installation:
    1. Install the dependencies

    2. Download the pretrained models here: https://drive.google.com/file/d/0Bx4sNrhhaBr3TDRMMUN3aGtHZzg/view?usp=sharing
    
        Then extract those files into models

    3. Run main.py

## Requirements:
    Python3 (3.5 ++ is recommended)

## Dependencies:

    opencv3

    numpy

    tensorflow ( 1.1.0-rc or  1.2.0 is recommended )


## Howto:
    `python3 main.py` to run the program
    `python3 main.py --mode "input"` to add new user. Start turning left, right, up, down after inputting the new name. Turn slowly to avoid blurred images

To achieve best accuracy, please try to mimick what I did here in this gif while inputting new subject:
    
![GIF Demo](https://media.giphy.com/media/3o7aD7CZ6C3RLCvLgs/giphy.gif)

        
### Flags:
   `--mode "input"` to add new user into the data set
    


## General Information:
Project: Facial Recogition


### Framework and Libs:

Tensorflow: The infamous Google's Deep Learning Framework

OpenCV: Image processing (VideoCapture, resizing,..)

### Additional Libs :
    SQLlite
    datetime


## Credits:
    -  David Vu from : https://github.com/vudung45
    -  Pretrained models from: https://github.com/davidsandberg/facenet
