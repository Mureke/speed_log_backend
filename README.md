## Speed log
This is a simple flask app for saving speed test results and returning them from REST API

### How to run
`$ export FLASK_APP=app.py`

`$ export FLASK_ENV=develop`

`$ export ENV=dev`
 
#### Dev server:

`$ flask run`

#### Speed logger:
`$ flask commands speed-test`


#### Overwriting configurations:
This app is using `dotenv` to overwrite basic configuration. <br> 
To overwrite basic configuration just create a new file named `.env` to project root and 
list your custom configurations there.