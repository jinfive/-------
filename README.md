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
## Team introduction
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


Installation
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
  <img src="https://img.shields.io/badge/github-%23181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" style="margin-right: 10px;">
  <img src="https://img.shields.io/badge/intellijidea-%23000000?style=for-the-badge&logo=intellijidea&logoColor=white" alt="IntelliJ IDEA">
</div>
<br><br>
Development
<br>
<div style="display: flex; align-items: center;">
  <img src="https://img.shields.io/badge/JAVA-1572B6?style=for-the-badge&logo=JAVA&logoColor=white" style="margin-right: 10px;">
  <img src="https://img.shields.io/badge/gradle-%2302303A?style=for-the-badge&logo=gradle&logoColor=white" alt="gradle"style="margin-right: 10px;">
  <img src="https://img.shields.io/badge/mysql-%234479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="mysql" style="margin-right: 10px;">
</div>

<br><br>
Communication
<br>
<div style="display: flex; align-items: center;">
  <img src="https://img.shields.io/badge/notion-%23000000?style=for-the-badge&logo=notion&logoColor=white" alt="notion"style="margin-right: 10px;">
  <img src="https://img.shields.io/badge/googledrive-%234285F4?style=for-the-badge&logo=googledrive&logoColor=white" alt="googledrive" style="margin-right: 10px;">
  <img src="https://img.shields.io/badge/Slack-%234A154B?style=for-the-badge&logo=Slack&logoColor=white" alt="Slack" style="margin-right: 10px;">
</div>


## etc
<a href="https://drive.google.com/file/d/166SGvni65tOsIooB8u-ZIrnwMhnn5Uy-/view?usp=drive_link" target="_blank">final report >> https://drive.google.com/file/d/166SGvni65tOsIooB8u-ZIrnwMhnn5Uy-/view?usp=drive_link</a>

<a href="https://www.youtube.com/watch?v=jF26-mtclxE" target="_blank">Demonstration video >> https://www.youtube.com/watch?v=jF26-mtclxE</a>
