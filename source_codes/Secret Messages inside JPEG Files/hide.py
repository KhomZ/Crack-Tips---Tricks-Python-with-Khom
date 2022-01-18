'''
@author: KhomZ
This is how we can hide Secret Messages Inside of JPEG Files with Python
without changing anything about the actual image.

If you open images using Hex Editor u will see
start with FF D8
and
ending with FF D9

'''

# with open('lady.jpg', 'ab') as f:
#     f.write(b"Hello ikhomkodes! This is a secret message. Please Keep it safe.")  # b for bytes

# how to get the information from that image
with open('lady.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)
    print(f.read())
