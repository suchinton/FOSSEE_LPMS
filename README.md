# FOSSEE_LPMS (FOSSEE Linux Package Management System)

Made as per the specificatinos provided by FOSSEE for the **[3rd Task: Linux Package Management System](https://fossee.in/semester-internship/2023)**

FOSSEE_LPMS is a packaged executable installer/Front-end for **[Verilator](https://verilator.org/guide/latest/overview.html)**, a free and open-source software tool which converts Verilog (a hardware description language) to a cycle-accurate behavioral model in C++ or SystemC

it can be freely distributed for any Linux-based platform (OS), it is written in Python using the PyQT5 library and packaged as an Appimage.

## ScreenShots
![2023-01-26-184214_563x458_scrot](https://user-images.githubusercontent.com/75079303/214845665-3f921d26-6f24-4566-a4cc-a98833958ce5.png) ![2023-01-26-184221_563x458_scrot](https://user-images.githubusercontent.com/75079303/214845682-0704f3e7-5ef7-4668-b313-44971b83e5f0.png)
---
## Functions
- Accepts Verilog & C++ Files to create executable object
- Checks if Verilator is installed on the system 
- Checks for supported versions of Verilator
- Provides automated installation of latest Stable Release of Verilator

## Build from Source

**IMPORTANT**: Do this only if you wish to build from Source

### Clonign Repo

```bash
git clone https://github.com/suchinton/FOSSEE_LPMS.git
```

### Resolving Dependencis on Ubuntu 

Downlad equilant packages on other Linux Distributions
Resolves dependencies for Verilator as well but dosen't insall it by default
(Refer to [Verilator install instruction for latest version](https://verilator.org/guide/latest/install.html#package-manager-quick-install))

```bash
cd ./FOSSEE_LPMS/

bash ./Ubuntu_install_script.sh
```

### Make Appimage (FOSSEE_GUI-x86_64.AppImage)

```bash
bash ./make_appimage.sh
```
---

## Download Appimage

To use the platform independent Appimage package
Download the latest release from github

- To run from terminal run 
  ```bash
  cd /Path/To/Downloaded/Appimage/
  
  chmod +x ./FOSSEE_GUI-x86_64.AppImage
  
  ./FOSSEE_GUI-x86_64.AppImage
  ```
- To run from file manager
  - Open prefferd file manager
  - Navigate to file (FOSSEE_GUI-x86_64.AppImage)
  - Right click -> Select Properties -> Make Executable
  - Double Click to Launch
   
- To Add to Application Launcher (Optional)
  - refer to [AppImageLauncher](https://github.com/TheAssassin/AppImageLauncher)
 
---

## Dependencies

FOSSEE_GUI has zero dependencies after compilation. Thanks to the following projects/tools for making this possible:

- [Verilator](https://verilator.org/guide/latest/overview.html)
- [pyinstaller](https://pyinstaller.org/en/stable/installation.html) (pip)
- [PyQt5](https://pypi.org/project/PyQt5/) (pip)
- [Appimagetool](https://appimage.github.io/appimagetool/) (Appimage)
