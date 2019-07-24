from flask import Flask, render_template
import json
import urllib.request

app = Flask(__name__)

@app.route('/')
def hello_name():
    # Url that leads to the "Astronomy Picture of The Day"
    apodUrl = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

    # Access the entire URL by combining the two above strings.
    urlObject = urllib.request.urlopen(apodUrl)

    # Get the JSON that was on the website, and store it into this object
    jsonObject = urlObject.read()

    # read in the JSON into a python data structure
    jsonDict = json.loads(jsonObject.decode('utf-8'))

    return render_template('index.html', myName = jsonDict['url'])

if __name__ == '__main__':
    app.run()