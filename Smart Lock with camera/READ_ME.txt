Smart lock with face reconition project, an embedded system project made by Nasser Obeid
and Yousef el-Helo. the project consists of a python code for face recogonition and
the arduino code for controlling the arduino. it works by serial communication between
python and arduino.

Setup steps:

1. upload the sketch to the arduino board, and take note on what COM port it's 
connected to, make sure the required libraries are installed in the 'requirements.txt' file.

2. run the 'main.py' after uploading the sketch, run the code and make sure to
select the correct port the arduino board is connected with. and also make a webcam
is also connected to the system(opencv automatically detects the camera connected to the 
system).

3. use the keyboard to control the action what action to take on the camera window:
pressing 'q' on the keyboard:
quits the program.

pressing 'n' on the keyboard:
makes a new user and saves there face to the database.

pressing 'r' on the keyboard:
to check if the user is a registered user and is recognized by the system.

4. enjoy!!!

this project was submitted to the administration as a part of partaking in the 
embedded system course.

Nasser Obeid
Yousef el-Helo

special thanks fo DR. Aryaf el-Adwan and Enas Ramadan for the opportunity!!
