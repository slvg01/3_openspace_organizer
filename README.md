# Project Objective : Create an Openspace Organizer for office or more


## Main features 
existing on the main branch : 
- The program takes an XL list of people as argument
- The program distributes people randomly on existing tables
- The program deal with the possibility of having too many people in the room
- The program display the number of people in the room & the number of seats that are left
- the code output a dataframe with the final repartition (name) in the terminal and in an xl file (output_file.csv)
Additional features in that branch : 
- possibility to outsource the room setup from a config.json file (nb of table, nb of people per table) (Done)
- possibility to change interactively the setup and rerun the program (Not done yet)
- possibility to add someone in the room (for instance, a new colleague arriving or someone being late) (Not done yet)
- possibility to add a table if the room is full (Not done yet)
- possibility to integrate an Excel "conditions" list → X wants to be seated next to Y, or X doesn't want to be seated next to Y (Not done yet)
- Improve the algorithm to avoid having someone alone at a table (Not done yet)


![Alt text](image.png)


## Installation and running
- running :   openspace-organizer> python main.py
- src folder contains the classes and functions script 
- input is a colleagues.csv file (default one is  inthe folder) 
- you can customize the nb of tables and seats per table in the config.json file 
- built on python version 3.11.5
