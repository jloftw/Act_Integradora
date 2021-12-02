# Modelacion_Act_Integradora
### Jorge Alejandro Lopez Sosa - A01637313

## Requirements
### Server:
- agentpy
- websockets

To install agentpy and websockets run:
```pip3 install agentpy websockets```

### Unity:
- [NativeWebSocket](https://github.com/endel/NativeWebSocket)
- [NavMeshComponents](https://github.com/Unity-Technologies/NavMeshComponents)

To install NativeWebSocket, follow the instructions on the GitHub page and to install NavMeshComponents, clone the reposotory into the ```/Assets``` folder of your Unity project.

## Run program
Find ```server.py``` within the Server folder and run the following command: ```python3 server.py```

Then run the Unity scene ```Simulation``` within the ```/Assets/Scenes``` folder of the unity package.
