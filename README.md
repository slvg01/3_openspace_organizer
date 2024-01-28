# Target : Create an Openspace Organizer - for training purpose


## Details 

### The Openspace Organizer is able to randomly assign people to a spot in the open space. The algorythm and code themselves must 
- Make good use of classes using the object-oriented programming (OOP) paradigm
- Use imports in a clean way
- Use a clean architecture
- Read data from an Excel file
- Structure and present a GitHub project


## Installation and running
- built on python version 3.11.5: [Python interpreter](https://www.python.org/downloads/) at minima is needed  or [IDE](https://code.visualstudio.com/download)
- clone the full repo including the src folder that contains the class and function script 
- script are built with relative path thus launch from:   openspace-organizer> python main.py
- you must have a csv file with the names to load in the main directory. A default file callded colleagues.csv is preloaded. If you change that file name please change the load instruction accordingly on main.py
- you may change the nb of seats per table in the table.py script, class Table argument - default is 4 
- you change the nb of table in the openspace.py script class OpenSpace argument -default is 6  

## Main features (on the main branch)
The default setup of the open space is 6 tables of 4 seats → 24 seats
- The program takes an XL list of colleagues file as argument to the load in the main.py script
- The program distributes at random the people on the existing tables and says how many seats are left
- The program can gracefully deal with the possibility of having too many people in the room
- The program has functionality to display the repartition, the number of people in the room, the number of seats that are left
- the code will output a dataframe with the final repartition (name) by table in the terminal when ran and a related xl file called output_file.csv


![Alt text](image.png)



## Nice to have features (on the NTH branch if getting there) - not done yet 
- possibility to change interactively the setup and rerun the program
- possibility to outsource (part of) the room setup from a config.json file
- possibility to add someone in the room (for instance, a new colleague arriving or someone being late)
- possibility to add a table if the room is full
- possibility to integrate an Excel "conditions" list → X wants to be seated next to Y, or X doesn't want to be seated next to Y
- Improve the algorithm to avoid having someone alone at a table
