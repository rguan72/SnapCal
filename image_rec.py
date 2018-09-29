import base64 # testing purposes only
import io
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

class Flier(object):
    def __init__(self, image): # expects base64
        #self.image = image.read()
        self.image = image

    def ocr(self):
        image = types.Image(content=self.image)
        response = client.text_detection(image=image)
        #print('Full Text: {}'.format(response.full_text_annotation.text))
        return response.full_text_annotation.text

# Below: testing purposes only
# def encode_image(imagepath):
#     with io.open(imagepath, 'rb') as image_file:
#         image_content = imagefile.read()
#     return base64.b64encode(image_content)

filename = '/home/richard/Downloads/IMG_0735.JPG'
with io.open(filename, 'rb') as image_file:
    image_content = image_file.read()
#encoded = base64.b64encode(io.open(filename, 'rb'))
#encoded_content = encoded.read()
#test_im = Flier(encoded) # using base64
test_im = Flier(image_content) # using file
test_im.ocr()
