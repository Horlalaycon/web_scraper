#!/usr/bin/python
# Web Scraper Created by sys_br3ach3r GitHub

import requests
import argparse
from bs4 import BeautifulSoup

banner = r"""
---------------------------------------------------------------------- 
|-|----------------------------------------------------------------|-|
(~| __        __   _                                               |~)
|~) \ \      / /__| |__        ___  ___ _ __ __ _ _ __   ___ _ __  (~| 
(~|  \ \ /\ / / _ \ '_ \ _____/ __|/ __| '__/ _` | '_ \ / _ \ '__| |~)
|~)   \ V  V /  __/ |_) |_____\__ \ (__| | | (_| | |_) |  __/ |    (~|
(~|    \_/\_/ \___|_.__/      |___/\___|_|  \__,_| .__/ \___|_|    |~)
|~)                                              |_|               (~|
|-|----------------------------------------------------------------|-| 
(~|  Purpose: for scraping data like links,texts,titles,scripts &  |~)
|~)  input-fields on website.                                      |~)
|-|----------------------------------------------------------------|-|
|~)     Created by: sys_br3ach3r                                   (~|
|-|----------------------------------------------------------------|-|
(~|                 A.K.A @Horlalaycon @github                     |~)
----------------------------------------------------------------------
                             +---------+         -----
                            +-----------+        |   |
                           +-------------+       -----
======================================================================
======================================================================
"""


# web Scraper Object
class WebScraper:
    def __init__(self, url):
        self.url = url

        self.headers = {'User-Agent': 'Mozilla/5.0'}

        self.response = requests.get(url, headers=self.headers)

        self.soup = BeautifulSoup(self.response.content, 'html.parser')

# data type methods
    def get_title(self):
        return self.soup.title.text

    def get_links(self):
        links = []
        for link in self.soup.find_all('a'):
            links.append(link.get('href'))
        return links

    def get_images(self):
        images = []
        for img in self.soup.find_all('img'):
            images.append(img.get('src'))
        return images

    def get_text(self):
        return self.soup.get_text()

    def get_tables(self):
        tables = []
        for table in self.soup.find_all('table'):
            tables.append(table)
        return tables

    def get_forms(self):
        forms = []
        for form in self.soup.find_all('form'):
            forms.append(form)
        return forms

    def get_scripts(self):
        scripts = []
        for script in self.soup.find_all('script'):
            scripts.append(script.get('src'))
        return scripts

    def get_css(self):
        css = []
        for link in self.soup.find_all('link', rel='stylesheet'):
            css.append(link.get('href'))

        return css

    def get_meta(self):
        meta = []
        for meta_tag in self.soup.find_all('meta'):
            meta.append((meta_tag.get('name'), meta_tag.get('content')))
        return meta

    def get_input(self):
        inputs = []
        for input_tag in self.soup.find_all('input'):
            inputs.append((input_tag.get('name'), input_tag.get('value')))
        return inputs

    def get_iframe(self):
        iframes = []
        for iframe in self.soup.find_all('iframe'):
            iframes.append(iframe.get('src'))
        return iframes

    def get_headings(self):
        headings = []
        for heading in self.soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            headings.append(heading.text)
        return headings

    def get_paragraphs(self):
        paragraphs = []
        for paragraph in self.soup.find_all('p'):
            paragraphs.append(paragraph.text)
        return paragraphs

    def get_lists(self):
        lists = []
        for list_item in self.soup.find_all(['ul', 'ol', 'dl']):
            lists.append(list_item.text)
        return lists

    def get_videos(self):
        videos = []
        for video in self.soup.find_all('video'):
            videos.append(video.get('src'))
        return videos

    def get_audio(self):
        audio = []
        for audio_tag in self.soup.find_all('audio'):
            audio.append(audio_tag.get('src'))
        return audio

    def get_canvas(self):
        canvas = []
        for canvas_tag in self.soup.find_all('canvas'):
            canvas.append(canvas_tag.get('id'))
        return canvas

    def get_svg(self):
        svg = []
        for svg_tag in self.soup.find_all('svg'):
            svg.append(svg_tag.get('id'))
        return svg

    def get_math(self):
        math = []
        for math_tag in self.soup.find_all('math'):
            math.append(math_tag.get('id'))
        return math

    def get_frameset(self):
        frameset = []
        for frameset_tag in self.soup.find_all('frameset'):
            frameset.append(frameset_tag.get('id'))
        return frameset

    def get_frame(self):
        frame = []
        for frame_tag in self.soup.find_all('frame'):
            frame.append(frame_tag.get('id'))
        return frame

    def get_noscript(self):
        noscript = []
        for noscript_tag in self.soup.find_all('noscript'):
            noscript.append(noscript_tag.get('id'))
        return noscript


# main function to call all other methods
def main():
    data = ''
# parsing arguments
    parser = argparse.ArgumentParser(prog="Web-Scraper", description=' for scraping data like links,texts,titles on website', formatter_class=argparse.RawTextHelpFormatter, epilog="python scraper.py -u https://example.com -op 2 -o links.txt")
    parser.add_argument('-u', '--url', help='URL to scrape data from', required=True)
    parser.add_argument('-o', '--output', help='Output result to file')
    parser.add_argument('-op', '--option', type=int, help='''
Choose data-type to scrape (1-22): (e.g --option 2) 

        [1 - Get Title]
        [2 - Get Links]
        [3 - Get Images]
        [4 - Get Text]
        [5 - Get Tables]
        [6 - Get Forms]
        [7 - Get Scripts]
        [8 - Get CSS]
        [9 - Get Meta tags]
        [10 - Get Input fields]
        [11 - Get Iframes]
        [12 - Get Headings]
        [13 - Get Paragraphs]
        [14 - Get lists]
        [15 - Get videos]
        [16 - Get audio]
        [17 - Get canvas]
        [18 - Get SVG]
        [19 - Get math]
        [20. Get frameset]
        [21 - Get frame]
        [22 - Get noscript]
''', required=True)

    args = parser.parse_args()

    scraper = WebScraper(args.url)
# Processing user option
    if args.option == 1:
        data = scraper.get_title()

    elif args.option == 2:
        data = scraper.get_links()        

    elif args.option == 3:
        data = scraper.get_images()

    elif args.option == 4:
        data = scraper.get_text()

    elif args.option == 5:
        data = scraper.get_tables()

    elif args.option == 6:
        data = scraper.get_forms()

    elif args.option == 7:
        data = scraper.get_scripts()

    elif args.option == 8:
        data = scraper.get_css()

    elif args.option == 9:
        data = scraper.get_meta()

    elif args.option == 10:
        data = scraper.get_input()

    elif args.option == 11:
        data = scraper.get_iframe()

    elif args.option == 12:
        data = scraper.get_headings()

    elif args.option == 13:
        data = scraper.get_paragraphs()

    elif args.option == 14:
        data = scraper.get_lists()

    elif args.option == 15:
        data = scraper.get_videos()
        
    elif args.option == 16:
        data = scraper.get_audio()

    elif args.option == 17:
        data = scraper.get_canvas()

    elif args.option == 18:
        data = scraper.get_svg()

    elif args.option == 19:
        data = scraper.get_math()

    elif args.option == 20:
        data = scraper.get_frameset()

    elif args.option == 21:
        data = scraper.get_frame()

    elif args.option == 22:
        data = scraper.get_noscript()

    else:
        print("Invalid option! use options specified in the help menu, e.g (--option 2) for scraping links")

    if args.output:
        print("+------------------------------+")
        print("|        Data Found[+]         |")
        print("+------------------------------+")
        print(data)

        output_file = args.output + ".txt"
        with open(output_file, 'w') as f:
            if isinstance(data, list):
                for item in data:
                    f.write(str(item) + '\n')
            else:
                f.write(data)
        print(f"+----------------------------------------+")
        print(f'|     Output saved to {args.output}      ')
        print(f"+----------------------------------------+")
    else:
        print("+------------------------------+")
        print("|        Data Found[+]         |")
        print("+------------------------------+")
        for i in data:
            print(f" {i}")


if __name__ == "__main__":
    print(banner)
    # handling exception
    try:
        main()
    except EnvironmentError as e:
        print("f+---------------------------------------+")
        print(f" Error: {e} \nCheck your internet connection ")
        print(f"+---------------------------------------+")
