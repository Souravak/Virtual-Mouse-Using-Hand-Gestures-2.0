

# Vision-Based Computer Cursor Control and Authentication Using Hand &nbsp;[![](https://img.shields.io/badge/python-3.10.5-blue.svg)](https://www.python.org/downloads/) [![platform](https://img.shields.io/badge/platform-windows-green.svg)](https://github.com/Souravak/Virtual-Mouse-Using-Hand-Gestures-2.0) 

Human-computer interaction (HCI) has become an instrument of great importance in bringing the idea that the link between a user and a computer should look more and more like one between two human beings. Research in human-computer interaction field is done by innovation in the field of software tools, studies of computer-supported work, or intelligent agents. This project designs a vision-based interface for regulating a computer mouse via 2D hand gestures. Also, a vision-based system to control various mouse activities such as left and right clicking, scrolling, zoom in and zoom out using hand gestures to make the interaction more efficient and reliable. This method mainly focuses on the use of a Web Camera to develop a virtual HCI application in an effective manner. In this method initially the hand is recognized using OpenCV and MediaPipe and then pixel to pixel mapping is done to trace the movement of hand. Using this application, differently abled people can easily use a computer system for daily usage with minimum effort. This application reduces the usage of external hardware in such a way that the motion of fingers in front of a camera will result in the necessary operation on the screen


Note: Use Python version: 3.10.5 or below

# Features
 _click on dropdown to know more_ <br>

### Gesture Recognition:
<details>
<summary>Neutral Gesture</summary>
 <figure>
  <figcaption>Neutral Gesture. Used to halt/stop execution of current gesture. Open all fingers</figcaption>
</figure>
</details>
 

<details>
<summary>Move Cursor</summary>
  <figcaption>Cursor is assigned to the midpoint of index and middle fingertips. This gesture moves the cursor to the desired location. Speed of the cursor movement is proportional to the speed of hand.</figcaption>
</details>

<details>
<summary>Left Click</summary>
 <figcaption>Gesture for single left click</figcaption>
</details>

<details>
<summary>Right Click</summary>
 <figcaption>Gesture for single right click</figcaption>
</details>

<details>
<summary>Double Click</summary>
 <figcaption>Gesture for double click</figcaption>
</details>

<details>
<summary>Scrolling</summary>
 <figcaption>Dynamic Gestures for horizontal and vertical scroll. The speed of scroll is proportional to the distance moved from center of the screen to up or down.</figcaption>
</details>

<details>
<summary>Drag and Drop</summary>
 <figcaption>Gesture for drag and drop functionality. Can be used to move/tranfer files from one directory to other.</figcaption>
</details>

<details>
<summary>Multiple Item Selection</summary>
 <figcaption>Gesture to select multiple items</figcaption>
</details>

<details>
<summary>Volume Control</summary>
 <figcaption>Dynamic Gestures for Volume control. The rate of increase/decrease of volume is proportional to the distance moved from center of the screen to up or down.</figcaption>
</details>

<details>
<summary>Brightness Control</summary>
 <figcaption>Dynamic Gestures for Brightness control. The rate of increase/decrease of brightness is proportional to the distance moved from center of the screen to up or down. </figcaption>
</details>

<details>
<summary>Zoom Control</summary>
 <figcaption>Dynamic Gestures for Zoom control. The rate of increase/decrease of brightness is proportional to the distance moved from center of the screen to up or down. </figcaption>
</details>

<summary>Close Control</summary>
 <figcaption>Dynamic Gestures for Close control.</figcaption>
</details>

# Getting Started

  ### Pre-requisites
  
  Python: (3.6 - 3.20.5)<br>
  
  ### Procedure
  ```bash
  git clone https://github.com/Souravak/Virtual-Mouse-Using-Hand-Gestures-2.0.git
  ```
  For detailed information about cloning visit [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).
  
  Step 1: 
  ```bash
  py -3.10 -m venv venv 
  ```
  
  Step 2:
  ```bash
  .\venv\Scripts\Activate.ps1
  ```
  
  Step 3:
  ```bash
  pip install -r requirements.txt
  ```
  
  Step 4:
  ``` 
  cd to the GitHub Repo till src folder
  ```
  Command may look like: `cd C:\Users\.....\VIRTUAL-MOUSE-USING-HAND\Phase-1\Code\`
  
  Step 5:
  
  For running :
  ```bash 
  python hand_detection_new_v12.py
  ```

  

  
# Collaborators
  | |  |  |  |  |
  | ------------- | ------------- | ------------- | ------------- | ------------- |
  | Sourav A K | [GitHub](https://github.com/souravak) | [Email](mailto:souravak211@gmail.com) | [LinkedIn](https://www.linkedin.com/in/souravak/) | [Instagram](https://www.instagram.com/s.r.v.a.k) |
  | Mithun K | [GitHub](https://github.com/souravak) | [Email](mailto:souravak211@gmail.com) | [LinkedIn](https://www.linkedin.com/in/souravak/) | [Instagram](https://www.instagram.com/__mithun___k/) |
  | Adithyan S P | [GitHub](https://github.com/souravak) | [Email](mailto:souravak211@gmail.com) | [LinkedIn](https://www.linkedin.com/in/souravak/) | [Instagram](https://www.instagram.com/_adi.sp_/) |
  
