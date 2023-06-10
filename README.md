# Plugget Unreal plugin

Unreal plugin to search & install [plugget](https://github.com/hannesdelbeke/plugget) packages 

![image](https://github.com/plugget/plugget-qt-addon/assets/3758308/0752c140-5b26-452e-81ac-fc4e36ccdb23)<br>

relies on [plugget-qt-search](https://github.com/hannesdelbeke/plugget-qt-search)

### Install instructions
1. Unzip & add the plugin folder to the unreal plugins folder
2. Restart or open Unreal
3. Enable the `plugget` plugin from the menu `edit/Plugins`


### usage instructions
- The UI can be opened from the menu or toolbar if you set the env vars (see below)
- Search for plugget packages, and click install to install the selected version
- List installed packages with the list button

### Environment variables
you can control how plugget loads on startup with these env vars
- `PLUGGET_UE_TOOL_BAR_BUTTON`: default to `0`, if set to `1`, adds a button to the tool bar to launch the UI 
- `PLUGGET_UE_MENU`:  default to `0`, if set to `1`, adds a menu entry under Tools/Plugget **TODO** ⚠️not yetimplemented, verify path

### Support

If this tool is helpfull, you can ⭐ star it on the github page,
just click the ⭐ star button in the top-right of this page.
