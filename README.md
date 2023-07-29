In this project, we explore using the face_recognition library with python to make a 
face recognition application that records attendance of known faces in real time. 

Inside of this project, there are 2 main files that utilize facial regonition: 
'AttendanceProject.py' and 'faceRec1.py', both located inside of the 'env' folder. 
The 'AttendanceProject.py' file is the main code for the project, and the 'faceRec1.py' 
file contains code that was used for initial testing of the face_recognition library.

When the main code (AttendanceProject.py) is running, upon recognizing one of the faces 
it knows (which are aggregated from the files in the 'facesToLookFor' folder), it 
records the name of the face and the time of recognition inside of the Attendance.csv 
file.

In order to run this project on your machine, after cloning the directory into Visual 
Studio Code, you will first need to install the dependencies necessary for the project. 
You can do this by running either the 'setup.zsh' file (for mac users) or the 'setup.bat' 
file (Windows users). To do this, inside of VS Code, on the top bar, click 'Terminal' and 
select 'New Terminal'. Then enter './setup.<filetypeForMachine>' and the dependencies 
should be installed. Finally, right click AttendanceProject.py inside of env, and chose 
'Run Python File in Terminal'.

The project should now be running! Note that you may need to allow access to your 
computer's Webcam for this project. If your Webcam is enabled, you should see a Webcam 
window pop up. You can now look up an image of anyone in any of the images in the 
'facesToLookFor' directory, and if you point your webcam towards that image, the webcam 
should put a green box around the face in real time and add it to the 'Attendance.csv' 
file along with the time it was seen. Also note that the names used to identify faces in 
real time are taken from the filenames in the 'facesToLookFor' folder, so these images 
should be named with the names of the people that we would like to look for. 

Thanks for trying my project, and have fun!

