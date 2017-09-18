import json
import urllib2

cityName = raw_input('Choose a city: ')

origCityName = cityName
cityName = cityName.lower().replace(" ", "")

api = "https://publicdata-weather.firebaseio.com/" + cityName + "/currently.json"
get = urllib2.urlopen(api).read()
data = json.loads(get)

if data is None:
    print "Error, " + origCityName + " is not a valid city."
else:
    temp = data['temperature']
    clouds = data['summary']

    print 'It is currently ' + str(temp) + u'\u00b0' + ' F and ' + clouds.lower() +' in ' + origCityName