# Plugget Unreal plugin

Unreal plugin to search & install [plugget](https://github.com/hannesdelbeke/plugget) packages 

![image](https://github.com/plugget/plugget-qt-addon/assets/3758308/0752c140-5b26-452e-81ac-fc4e36ccdb23)<br>

relies on [plugget-qt-search](https://github.com/hannesdelbeke/plugget-qt-search)

### Install instructions
1. Unzip & add the plugin folder to the unreal plugins folder
2. Restart or open Unreal
3. Enable the `plugget` plugin from the menu `edit/Plugins`


### usage instructions
the UI can be opened with the command 
```python
import plugget_search_widget
w = plugget_search_widget.show()  # store reference in w, to prevent garbage collection
```

If this tool is helpfull, you can ⭐ star it on the github page,
just click the ⭐ star button in the top-right of this page.
