# BETTER-PARKING

<div align="center"> <img align="center" alt="" src="" height='95' width='380'> </a> </div>

Objective: 
* In the current implementation of multi-level parking slots, it is extremely difficult to figure out where an empty slot may be available, this leads to extreme time delays in finding a parking slot, thus leading to wastage of time. 
* Navigating around each floor, in search of a parking slot is extremely energy consuming and tiring as well, our project aims at improving the overall experience of mall customers, by making the beginning - parking much more convenient. 
* Travel within a parking complex is very slow, and a lot of distance is generally covered in trying to find an empty slot, this leads to fuel wastage due to extremely low mileage travel. * Extra spendings on parking charges due to delays caused by traffic within the complex and the difficulty of finding a parking slot.

Implementation: 
* Sensors will be installed on the ceiling, on top of each parking slot 
* The status of each slot (Vacant/Occupied) will be updated to the cloud in real-time. 
* The number of slots available on each floor is shown at the entrance of the parking lot, and each floor has a floor map displaying the location of the slots. 
* Thus, a visitor can easily find an empty slot and park conveniently.

Applications: 
* As we intend to build targeting large parking structures, our product can be highly scaled for any structure that needs to have large scale parking facilities. 
* Our product can also be improvised for two wheeler parking facilities as they also occupy a significant part of the parking structure. 
* Any person who owns a car and plans to visit a mall or a cinema theatre nearby knows the pain of finding the right parking spot. Our product could be used by almost anyone who wishes to park inside the parking facility in a short period of time. 
* Our product could help people reduce the stress created by the effort visitors have to put into finding a parking space, the traffic they have to deal with on the ramps between levels, and parking slot related quarrels, leading to a more peaceful experience overall. 
* People often worry about parking charges when visiting malls and other sites with multi-level parking, due to great reductions in parking delays, the cost of parking is reduced, this is another major societal impact.

## Tech Used
- **Frontend :** ReactJS, ElectronJS
- **Backend :** Express Js, Apache Kafka
- **Database :** Firebase
- **Version Control :** Git and GitHub


## How to Run Application

- Install Nodejs from the official website in your system if not available.

- Fork and Clone the Repo
```
$ git clone https://github.com/Saitama-Squad/better-parking.git
```
For backend: 

Create a new Virtual Environment:
```
python -m venv env
pip install -r ./requirements
```
Open 4 terminals 
```
python cloud/EventStream.py (1)
python device/cam.py (2)
python server/kafkaConsumer.py (3)
cd server && npm install && npm start (4)
```

For front end: 
```
npm install && npm start
```

## Demo Video:

<a href="https://youtu.be/kF3t6FgHUqw">Youtube</a>

## Team:

| S.No. | Name                        |  GitHub Username                                       |
| ----- | --------------------------- | ----------------------------------------------------   |
| 1.    | Lokesh N N                  |  [@lokeshn011101](https://github.com/lokeshn011101)    |
| 2.    | Moniesh Ravichandrran       |  [@Moniesh R](https://github.com/monieshravichandrran) |
| 3.    | Karun Anantharaman          |  [@Karun842002](https://github.com/Karun842002)        |
