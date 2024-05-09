# IoT-Project
Waste management system using a Raspberry Pi by Sigourney W.
______________________________________________
This project aims to create a waste-management system using python and physical hardware components. It measures trash levels collected in garbage cans, has a graphical user interface using Tkinter, and has a basic security system made from a simple button combination.


# Physical Components
- Breadboard + Jumper Wires
- ![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/3a377006-7723-4144-93e9-2273d6d268ba)

- Raspberry Pi (Model B)
- ![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/cbbfd50d-2dd3-4a21-a575-f2db210cbc7a)

- GPIO Extension Board + Wires
- ![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/9cf59ed3-1bdd-46b0-8dbf-4d2f35133b2e)

- Ultrasonic Sensor
- ![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/adef517f-ad9d-448f-b792-21724dee5604)

- LEDS (green and red)
- ![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/d7a6e729-ecff-44e4-98b2-a6e40169c325)

- Passive / Active Buzzer
- ![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/c2e43344-1ff5-4a2a-9278-ef167f244422)

- Red and Blue Buttons
- ![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/e066bc4b-2b44-42f9-a1a2-5b66836b1bfc)
- LED bar module
![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/580b72c2-0f3c-4e42-b9f6-02864acc4e92)



# Connections 
![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/9c85052d-746a-4f26-8e82-649b33d41983)




# GUI Mockup
![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/d7821bef-a40a-4484-a524-bc64002a8de1)


___________________________________________________________

# User Manual 
A document to showcase how the system works, and documents a few workarounds to some problems I had.
# The GUI
![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/c5cbe5cc-b0e4-49ae-8038-be254d4e4577)

# The Threshold Entry
- ![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/55040e9d-50c3-40aa-b02e-92cee7b34196)
- The user will enter the threshold they have in mind
- If the container's fullness is above or equal to the threshold, a message will appear notifying the user to empty the container.
- ![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/4ea3c2a1-3589-4be0-93ef-314b50901759)
# The Lid + Container Depth Entries
- ![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/462a7187-c4d2-4be3-80d7-735287e6d906)
- At the fault of my distance sensor being incredibly erratic (despite resting still on my container, the distance would fluctuate by +- 2 cm and sometimes spike!) I implemented this functionality so I could change it at will.
- The user will look at the current distance indicated (when their distance sensor is placed on a lid) and write down the depth in the respective entry area
- ![image](https://github.com/Novogenuata/IoT-Project/assets/159738542/038fb64e-612a-48d7-8ef4-dd2692492478)
- Once the user enters the depth, they will then calculate the lid height for the security system





