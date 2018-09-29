from flask import Flask, render_template, request
from image_rec import Flier
from add_cal import add_event

app = Flask(__name__)

@app.route('/')
def camera():
	### TESTING
	filename = '/home/richard/Downloads/IMG_0735.JPG'
	with io.open(filename, 'rb') as image_file:
	    image_content = image_file.read()
	#encoded = base64.b64encode(io.open(filename, 'rb'))
	#encoded_content = encoded.read()
	#test_im = Flier(encoded) # using base64
	test_im = Flier(image_content) # using file
	event_text = test_im.ocr()
	add_event("Event at 10 am")
	### TESTING END
	return render_template('camera_cp.html')

@app.route('/pictaken', methods=['POST', 'GET'])
def pictaken():
	return render_template('pictaken.html')


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
