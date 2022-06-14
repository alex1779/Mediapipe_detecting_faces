#Mediapipe_detecting_faces

## Requirements
```
mediapipe==0.8.9.1
opencv-python==4.5.5.64
```



## Installation on Windows using Anaconda
```
conda create -n Mediapipe_detecting_faces -y && conda activate Mediapipe_detecting_faces && conda install python=3.9.7 -y
git clone https://github.com/alex1779/Mediapipe_detecting_faces.git
cd Mediapipe_detecting_faces
pip install -r requirements.txt
```


## face_detection_picture.py
this is the direct result of implementation the mediapipe function called as mp.solutions.face_detection:

```
python face_detection_picture.py -i input/test.jpg -o output/
```

![Test](https://github.com/alex1779/Mediapipe_detecting_faces/blob/master/imgs/test.jpg)

 

## face_detection_picture_mesh.py
this is the result using mp.solutions.face_mesh:

```
python face_detection_picture_mesh.py -i input/test.jpg -o output/
```

![Test2](https://github.com/alex1779/Mediapipe_detecting_faces/blob/master/imgs/test2.jpg)


## differences
We can see the difference that the last result gives us:

![result](https://github.com/alex1779/Mediapipe_detecting_faces/blob/master/imgs/results2.jpg)

## License

Many parts taken from the cpp implementation from github.com/google/mediapipe

Copyright 2020 The MediaPipe Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.






