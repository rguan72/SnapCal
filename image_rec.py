class Flier(object):
    def __init__(image):
        from google.cloud import vision
        from google.cloud.vision import types
        vision_client = vision.Client()
        self.image = image

    def ocr():
        pass
