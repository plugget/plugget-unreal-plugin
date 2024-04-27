# Plugget Unreal plugin

Unreal plugin to search & install [plugget](https://github.com/plugget/plugget) packages 

![image](https://github.com/plugget/plugget-qt-addon/assets/3758308/0752c140-5b26-452e-81ac-fc4e36ccdb23)<br>

### dependencies
- [plugget-qt](https://github.com/plugget/plugget-qt)
- pip (have python installed and pip in the path)
- git (have git installed and in the path

### Install instructions
The following instructions are for Windows:
1. Install Python dependencies.
Install the dependencies to Unreal's engine folder:
```batch
set UE_FOLDER="D:\Program Files\Epic Games\UE_5.4"
set PYTHON_FOLDER=%UE_FOLDER%\Engine\Binaries\ThirdParty\Python3\Win64
cd /d %PYTHON_FOLDER%
python -m pip install PySide2 plugget-qt --target %PYTHON_FOLDER%\Lib\site-packages
```
3. Install git
```
winget install git.git
```
4. [Download](https://github.com/plugget/plugget-unreal-plugin/archive/refs/heads/main.zip) and Unzip
5. Copy the `plugget` folder inside the unzipped folder, to Unreal's plugins folder
6. Restart or open Unreal
7. Enable the `plugget` plugin from the menu `edit/Plugins`


### usage instructions
- The UI can be opened from the menu or toolbar if you set the env vars (see below)
- Search for plugget packages, and click install to install the selected version
- List installed packages with the list button

### Environment variables
you can control how plugget loads on startup with these env vars
- `PLUGGET_UE_TOOL_BAR_BUTTON`: default to `0`, if set to `1`, adds a button to the tool bar to launch the UI 
- `PLUGGET_UE_MENU`:  default to `0`, if set to `1`, adds a menu entry under Tools/Plugget **TODO** ⚠️not yetimplemented, verify path

### devs
- This repo contains the unreal plugin `Plugget`, and no Python modules.
- The Python dependencies it installs are `plugget` & `plugget_qt`

### Support

If this tool is helpfull, you can ⭐ star it on the github page,
just click the ⭐ star button in the top-right of this page.
