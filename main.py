from flask import Flask, render_template, request
from image_rec import Flier

import base64

app = Flask(__name__)

@app.route('/')
def camera():
	#image = request.args.get('image')
	#print "IMAGE: ", image
	return render_template('camera_cp.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
	name = request.form['name']
	email = request.form['email']
	site = request.form['site_url']
	comments = request.form['comments']
	return render_template(
	'submitted_form.html',
	name=name,
	email=email,
	site=site,
	comments=comments)

# Receive the image
@app.route("/receive", methods=["POST"])
def route_receive():
    data = request.form
    image = data["image"]
    # Chop off the first "english" part of the string so it's just b64
    image = image[image.find("base64,")+7:]
    print("Grabbed image!")
    save_undecoded_image(image, "image.jpg")
    print("Saved");
    return 'success'

#TEMPORARY
# Temporary thing for saving an undecoded b64 string
def save_undecoded_image(b64data, fname):
    with open(fname, "wb") as fh:
        fh.write(base64.b64decode(b64data))
        fh.close()


if __name__=="__main__":
    app.run(host  = "127.0.0.1",
            port  = 8080,
            debug = True
            )
