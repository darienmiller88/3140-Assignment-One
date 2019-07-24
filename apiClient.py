import json
import urllib.request
import webbrowser

#Url that leads to the "Astronomy Picture of The Day"
apodUrl = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

#Access the entire URL by combining the two above strings.
URLObject = urllib.request.urlopen(apodUrl)

#Get the JSON that was on the website, and store it into this object
JSONObject = URLObject.read()

#read in the JSON into a python data structure
JSONToDataStructure = json.loads(JSONObject.decode('utf-8'))

print("Here the stuff we found on the web!\n")
#print(JSONToDataStructure)

#"Prettify" The output of the JSON!
print(json.dumps(JSONToDataStructure, indent = 4, sort_keys=True))

input("Press enter to view NASA picture")
webbrowser.open(JSONToDataStructure['url'])
