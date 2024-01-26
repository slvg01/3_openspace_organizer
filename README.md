
# Target : Create an openspace Organizer for training purpose

## Details 
### The openspace organizer must be able randomly assigning people to a spot in the open space. The algorythm and code themselves must 
- Make good use of classes using the object-oriented programming (OOP) paradigm
- Use imports in a clean way
- Use a clean architecture
- Read data from an Excel file
- Structure and present a GitHub project


## Installation
- locally with Git 
- remotely on GitHub

## Must have features (on the main branch)
- You want to build a program that allows you to 
    - get a list of colleagues from an Excel file, 
    - place them randomly at the different tables of the open space.

- The default setup of the open space is 6 tables of 4 seats → 24 seats
    - The program takes a filepath as an argument to load the list of colleagues
    - The program distributes at random the people on the existing tables and says how many seats are left
    - The program can gracefully deal with the possibility of having too many people in the room
    - The program has functionality to display the repartition at any given point:
    - The number of people in the room
    - The number of seats that are left

## Nice to have features (on the nth branch is getting there)
- Once you have a basic program, you want to make it more interactive and more configurable. Here are a couple of suggestions:
    - Add the possibility to change interactively the setup and rerun the program
    - Add the possibility to outsource (part of) the room setup from a config.json file
    - Add the possibility to add someone in the room (for instance, a new colleague arriving or someone being late)
    - Add the possibility to add a table if the room is full
    - Add the possibility to integrate an Excel "conditions" list → X wants to be seated next to Y, or X doesn't want to be seated next to Y
    - Improve the algorithm to avoid having someone alone at a table
