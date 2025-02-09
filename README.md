# Power-analysis-control-system-for-home-smart-grid

## index

- [🖼️ project image](#-project-image)
- [📌 project information](#-project-information)
- [👥 Team introduction](#-Team-introduction)
- [🚀 Installation](#-Installation)
- [🌐 etc](#-etc)

## 🖼️ project image
<div align="center">
  <a href="https://ibb.co/2PnJDjf"><img src="https://i.ibb.co/wC0t9Kx/image.png" alt="image" border="0"></a>
  
  <a href="https://ibb.co/cvQym4n"><img src="https://i.ibb.co/X4tWwcR/image.png" alt="image" border="0"></a>


  <a href="https://ibb.co/DKc6f5t"><img src="https://i.ibb.co/YjnKBp3/image.png" alt="image" border="0"></a>
  <br>
  
</div>



## Repository visits
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjinfive%2FNewProject1&count_bg=%2379C83D&title_bg=%23555555&icon=java.svg&icon_color=%23D7C7C7&title=hits&edge_flat=false"/></a>

## 📌 project information
### KANGWON NATIONAL UNIVERSITY
📖 
capstone design
Development period:2024.03.04 ~ 2024.06.10
<br>
## 👥 Team introduction
Team leader:김흥주
<br>
team member:김진오,남강현,이채형

## Project Introduction
Development of Power-analysis-control-system-for-home-smart-grid
<ul>
  <li>Energy saving: Blocking standby power for home appliances used at home</li>
  <li>Abnormal current detection: Analyzes the current waveform of electronic products in use and cuts off power when an abnormality is detected.</li>
  <li>Home appliance classification: Classify home appliances by analyzing the current waveform of the home appliances currently in use.</li>
  <li>Accident prevention: Prevention of electrical accidents through outlets</li>
</ul>
<br>
<h2>Getting Started Guide</h2> 

Requirement
--
<ul>
  <ol>Python 3.13.0</ol>
  <ol>HTML5</ol>
  <ol>엑셀파일</ol>
  
</ul>


## 🚀 Installation
--

```
git clone https://github.com/jinfive/Power-analysis-control-system-for-home-smart-grid.git
```

```
cd /path/to/script/directory
python3 four_ver_rpi.py
```
Run script automatically when Raspberry Pi boots
```
nano launcher.sh
```
Enter the following
```
#!/bin/sh
cd /path/to/script/directory
python3 four_ver_rpi.py
```

```
chmod 755 launcher.sh
```

Edit crontab

```
sudo crontab -e
```
Add the following line to the end of the file

```
@reboot sh /path/to/launcher.sh &
```
## STACK 😸
<br>
Enviroment
<br>
<div style="display: flex; align-items: center;">
  <img src="https://img.shields.io/badge/raspberrypi-A22846?style=for-the-badge&logo=raspberrypi&logoColor=black" style="border-radius:10px">
  <img src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" style="border-radius:10px">
  
</div>
<br><br>
Development
<br>
<div style="display: flex; align-items: center;">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white" style="border-radius:10px">
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white" style="border-radius:10px">
  
</div>

<br><br>
Communication
<br>
<div style="display: flex; align-items: center;">
  <img src="https://img.shields.io/badge/kakaotalk-FFCD00?style=for-the-badge&logo=kakaotalk&logoColor=white" style="border-radius:10px">
</div>


## 🌐 etc
<a href="https://docs.google.com/spreadsheets/d/1SN1DLJhe6vC6NH8kIV9UJla5Z8VHP_Rl/edit?gid=429682832#gid=429682832" target="_blank">grades data >> https://docs.google.com/spreadsheets/d/1SN1DLJhe6vC6NH8kIV9UJla5Z8VHP_Rl/edit?gid=429682832#gid=429682832</a>

<a href="https://drive.google.com/file/d/1fBGJxnjC3L75YPvUwr9KR8rwJBDAOmsQ/view?usp=sharing" target="_blank">presentation >> https://drive.google.com/file/d/1fBGJxnjC3L75YPvUwr9KR8rwJBDAOmsQ/view?usp=sharing</a>

<a href="https://drive.google.com/file/d/1QAvmrWZJEv4rtOqb98qd1T-YY2MO6o6d/view?usp=sharing" target="_blank">final repot>> https://drive.google.com/file/d/1QAvmrWZJEv4rtOqb98qd1T-YY2MO6o6d/view?usp=sharing</a>
