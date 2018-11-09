import io
import base64
import os
import json
from subprocess import call
from flask import Flask, render_template, request, flash
from image_rec import Flier
from add_cal import EventAdder

app = Flask(__name__)

@app.route('/')
def camera():
    #image = request.args.get('image')
    #print "IMAGE: ", image
    return render_template('camera_cp.html')

# Receive the image
@app.route("/receive", methods=["POST"])
def route_receive():
    data = request.form
    image = data["image"]
    # Chop off the first "english" part of the string so it's just b64
    b64image = image[image.find("base64,")+7:]
    image = base64.b64decode(b64image)
    flier = Flier(image)
    text = flier.ocr_text()
    events = EventAdder.give_events(text)
    if events:
        for event in events:
            EventAdder.add_event(event)
    print "Grabbed image!"
    #save_undecoded_image(image, "image.jpg")
    print "Saved"
    return "success"

if __name__ == "__main__":
    # credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/richard/Downloads/SnapCalWeb-fb5b4f5bbee5.json"
    with open("hidden.json") as read_file:
        data = json.load(read_file)

    # export secret key
    app.secret_key = data["secret_key"]
    app.run(host  = "127.0.0.1",
            port  = 8080,
            debug = True
            )
