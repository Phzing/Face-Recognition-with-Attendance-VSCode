@echo off
python -m venv myenv
cd myenv\Scripts
call activate
pip install --upgrade pip
pip install cmake
pip install dlib
pip install face_recognition
pip install numpy
pip install opencv-python
cd ..\..