from flask import Flask, render_template, request
from image_rec import Flier

app = Flask(__name__)

@app.route('/')
def camera():
	return render_template('camera_cp.html')

@app.route('/pictaken', methods=['POST', 'GET'])
def pictaken():
	image = request.camera['image']
	print "IMAGE: ", image
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
