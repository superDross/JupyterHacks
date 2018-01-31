# JupyterHacks
Snippets of code add to functionality to Jupyter Notebook.

## Install
```bash
git clone https://github.com/superDross/JupyterHacks
export PYTHONPATH=$PYTHONPATH:/path/to/JupyterHacks
```

## Example
To embed a muted DailyMotion video that starts at the 90 seconds mark into your notebook:
```python
from JupyterHacks.hacks import EmbedVideo

EmbedVideo('http://www.dailymotion.com/video/x6415ml', start=90, mute=1)
```

To hide all code and only display output in your notebook:
```
from JupyterHacks.hacks import hide_code

hide_code()
```
