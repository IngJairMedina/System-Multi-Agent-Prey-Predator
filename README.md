# Multi-Agent Prey-Predator Simulator

This is a project developed for the Artificial Intelligence class of the Master's Degree in Electronic Engineering, Electronic Instrumentation option of the Benemerita Autonomous University of Puebla (BUAP).

This simulator was developed in Python language based on Multi-Agents, with the help of Flask, HTML and JavaScript tools.

This is a simulator based on the behavior of an ecocystem in which prey and predators coexist.

The objective of preparing this work is to study the causes and effects of the behavior of different species that interact in simulated environments, and to demonstrate that methodologies based on multi-agent systems have a close approximation in the behavior of prey-predator models. In this repository you can find the code developed.

### Requirements

To run the simulator it is necessary to have the following requirements, since some tools are used for correct operation.

```
Python-3.10.0(https://www.python.org/)
Numpy-1.20.1(https://numpy.org/install/)
Flask-2.0.3(https://flask.palletsprojects.com/en/2.0.x/)
```

## Make it work?

As we mentioned in the previous section, if you don't have what you need, you won't be able to run it.

The most important files in the project are:

* index.py
* prin.py
* index.py
* app.js
* main.html

To make the simulation start working, you must execute the index.py file, it will start in a localhost, the URL that you must place in the browser you prefer, will be provided by the python console.

To stop the simulator, just press Ctrl + C in the python console.

The files with the .py extension found inside the src folder are the interaction rules developed and the characteristics of the agents.

Inside the static folder you will find the JavaScript code file used to receive the relevant data from python and be able to display it on the Web page, you will also find the chart.js file which is used to graph the data obtained from the population in the Web page.

In the templates folder you will find the main.html file, this is the graphic part of the Web page.

## Cautions

You should not delete any files within the src folder, do not modify variable names, folders and files.

## Functioning

When the simulator is running on the left side the main canvas will be shown, within this the created agents will be shown, on the right side is the simulation area, here you can define which agents or species will appear in the simulation, you can select the color with which they will be represented, distinguishing between males and females, you must also put a number of agents per species, and finally you can select the speed of mating.

* There is a 50% chance that female and male agents will be created, this is random
* The pairing speed depends on the encounters between the agents within the simulation.

Below the main canvas is a secondary canvas, in which the current data of the population will be shown.

Once all the parameters have been configured to load all the data, the "LOAD" button must be pressed, this will create the agents that will start the simulation and assign their properties to them.

To start the simulation, click on the "EXECUTE" button, this will start the movement of the agents through their evaluation stage in which it is evaluated if there are agents close to an agent and according to this proximity it will be determined whether the The agent is of the same or a different species and with this the decision will be made as to whether the mating is evaluated or whether the hunt is evaluated, as the case may be.

## Prey-Predator Scheme

<img src="https://github.com/IngJairMedina/System-Multi-Agent-Prey-Predator/blob/main/Multi-Agent_Prey-Predator/src/static/cadena_alimenticia.png" width="400" >

## Results

As a main result, an application has been deployed using the Heroku platform, and it can be found at the following link: https://python-multi-agente.herokuapp.com/.

Ecosystem simulation and ecological modeling are fields in constant growth, having different applications between theoretical ecology, mathematics and computation, these simulations aim to model the dynamics of ecosystems in order to synthesize their understanding, and in this way to be able to predict how their behavior will change over time.

When comparing the proposed system with other models such as the Lotka-Volterra model, these are even more complex and take into account more factors, interaction rules and characteristics that define each agent to obtain results as similar as possible to the real behavior of an ecosystem.

## Authors

* **Dr. Salvador E. Ayala Raggi**-saraggi@gmail.com
* **Ing. Adriana Palacios Cruz**-adriana.palacios@alumno.buap.mx
* **Ing. José J. Medina García**-jose.medinag@alumno.buap.mx
