'''
@author: khomZ

Hide Images in JPEG Files
'''

import PIL.Image
import io

with open('ninja.jpg', 'ab') as f, open('FirstGame.exe', 'rb') as e:
    f.write(e.read())
