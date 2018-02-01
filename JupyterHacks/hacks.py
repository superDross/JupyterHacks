from IPython.display import HTML, IFrame
import requests
import bs4
import re


class DisplayVideo(IFrame):
    ''' Display a video into a Jupyter Notebook.'''

    def __init__(self, video_link, width=700, height=400, **kwargs):
        self.sites = {'youtube.com': 'https://www.youtube.com/embed/{}',
                      'vimeo.com': 'https://player.vimeo.com/video/{}',
                      'dailymotion.com': 'https://www.dailymotion.com/embed/video/{}'}
        self.video_link = video_link
        src = self._construct_src()
        super().__init__(src, width, height, **kwargs)

    def _construct_src(self):
        unwanted_substrings = 'www.|watch\?v\=|video\/'
        link = re.sub(unwanted_substrings, '', self.video_link)
        website, video = link.split('/')[-2:]
        src = self.sites[website].format(video)
        return src


class SlideShare(IFrame):
    ''' Display a linkdin slideshare in a jupyter notebook.'''

    def __init__(self, url, width=700, height=400, **kwargs):
        src = self._get_slideshare_embed_src(url)
        super().__init__(src, width, height, **kwargs)

    @staticmethod
    def get_url_text(url):
        ''' Download the text from a given link.'''
        req = requests.get(url)
        req.raise_for_status()
        html = bs4.BeautifulSoup(req.text, features='lxml')
        return html

    def _get_slideshare_embed_src(self, url):
        ''' Extract the embed link from the SlideShare URL.'''
        html = self.get_url_text(url)
        container = html.find('div', id='slideview-container')
        src = container.find('meta', itemprop='embedURL').get('content')
        return src


def hide_code():
    ''' Hides all code in a jupyter notebook and only displays code output. '''
    hide = HTML('''<script>
          function code_toggle() {
            if (code_shown){
              $('div.input').hide('500');
              $('#toggleButton').val('Show Code')
            } else {
              $('div.input').show('500');
              $('#toggleButton').val('Hide Code')
            }
            code_shown = !code_shown
          }
          $( document ).ready(function(){
            code_shown=false;
            $('div.input').hide()
          });
        </script>
        <form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>''')
    return hide
