'''
@author: khomZ

Hide Images in JPEG Files
'''

import PIL.Image
import io

# rb = reading bytes
with open('ninja.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)

    with open('newfile.exe', 'wb') as e:
        e.write(f.read())
