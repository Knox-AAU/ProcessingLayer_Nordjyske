# ProcessingLayer Nordjyske
## Getting started
To be able to run the program follow these steps:
1. Clone the GitHub repository.
2. Install all [requirements](#Requirements) on your system. We use the pip package manager.
3. Connect to the [API for the database](#connecting-to-the-db-api).
4. Run the program in Visual Studio Code by pressing F5 or running `main.py`.
5. If everything is working a menu should be printed in the console and steps 1-4 can be run if needed.

## Architecture
The architecture diagram for the whole program can be seen in the following figure:
![Architecture diagram](https://raw.githubusercontent.com/Knox-AAU/ProcessingLayer_Nordjyske/main/images/fullArchitectureDiagram.png)

## Requirements
The packages that the program needs to be able to run are written in the `requirements.txt` file. But the spacy package should be installed manually by following spaces installation guide [here](https://spacy.io/usage). Select the Danish trained pipeline and the pipeline for efficiency. We used the pip package manager. The generated commands can be run in a terminal, make sure they are installed in the same environment.

## Connecting to the DB API
Currently, the API for the database can be found on knox-node02.srv.aau.dk port 5502. To connect, SSH to the Knox node 2 server by running the following command in a terminal: `ssh -L 5501:localhost:5501 <username>@student.aau.dk@knox-node02.srv.aau.dk`. If any issues occur, more information can be found [here](https://wiki.knox.cs.aau.dk/en/Database/DocumentDataAPI/Introduction).

## Contact
Wiki link: [wiki.knox.cs.aau.dk/en/Preprocessing/GruppeA/GeneralInformation) \
Project link: [github.com/Knox-AAU/ProcessingLayer_Nordjyske](https://github.com/Knox-AAU/ProcessingLayer_Nordjyske/)
### Authors 2022
André Larsen Freiesleben \
Jakob Frederik Lykke \
Kasper Østergaard Nielsen \
Martin Langgaard Jacobsen \
Patrick Baghlani Reffsøe \
Peter Schwartz Lauridsen 
