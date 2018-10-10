from flask import Flask, render_template, request
from image_rec import Flier
import io
import base64
from add_cal import add_event

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
    flier.ocr_text()
    add_event(flier.ocr_text())
    print "Grabbed image!"
    #save_undecoded_image(image, "image.jpg")
    print "Saved"
    return 'success'

#TEMPORARY
# Temporary thing for saving an undecoded b64 string
def save_undecoded_image(b64data, fname):
    with io.open(fname, "wb") as fh:
        fh.write(base64.b64decode(b64data))
        fh.close()


if __name__=="__main__":
    app.run(host  = "127.0.0.1",
            port  = 8080,
            debug = True
            )
