class Flier(object):
    def __init__(self, image):
        # from google.auth import app_engine
        # import googleapiclient.discovery
        from google.cloud import vision
        from google.cloud.vision import types
        # credentials = app_engine.Credentials()
        # storage_client = googleapiclient.discovery.build(
        #     'storage', 'v1', credentials=credentials)
        #vision_client = vision.Client()
        self.image = image

    def ocr_text(self):
        from google.cloud.vision import types
        from google.cloud import vision

        client = vision.ImageAnnotatorClient()
        image = types.Image(content=self.image)
        response = client.text_detection(image=image)
        print('Full Text: {}'.format(response.full_text_annotation.text))
        return response.full_text_annotation.text
