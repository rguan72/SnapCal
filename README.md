# SnapCal Web
College student organization fairs can get really hectic:
![alt text][festifall]

[festifall]: https://github.com/rguan72/SnapCal/blob/master/md_images/festifall.jpg
UMICH festifall

During these fairs, you often pick up way too many fliers for events like mass meetings:
![alt text][fliers]

[fliers]: https://github.com/rguan72/SnapCal/blob/master/md_images/IMG_0779.JPG

# Development prerequisites
Make sure you have pip installed on your system.
Create a virtual environment with python version 2.7.


#Install necessary packages.
Run these commands within the project root directory (SnapCalWeb)
```
(myenv)$ pip install -t lib requirements.txt
```
# Run app
This is being developed and deployed on Google Cloud Platform.
```
(myenv)$ dev_appserver.py app.yaml
```
# Access the app as a consumer, not developer:
Search https://snapcalweb/appspot.com
