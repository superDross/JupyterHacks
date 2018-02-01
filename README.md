# JupyterHacks
Snippets of code add to functionality to Jupyter Notebook.

## Install
```bash
git clone https://github.com/superDross/JupyterHacks
pip3 install -r JupyterHacks/requirements.txt
export PYTHONPATH=$PYTHONPATH:/path/to/JupyterHacks
```

## Example
To display a muted DailyMotion video that starts at the 90 seconds mark into your notebook:
```python
from JupyterHacks.hacks import DisplayVideo

DisplayVideo('http://www.dailymotion.com/video/x6415ml', start=90, mute=1)
```

To hide all code and only display output in your notebook:
```python
from JupyterHacks.hacks import hide_code

hide_code()
```

To display a LinkedIn SlideShare presentation into your notebook:
```python
from JupyterHacks.hacks import SlideShare
SlideShare('https://www.slideshare.net/mbussonn/jupyter-a-platform-for-data-science-at-scale')
```
