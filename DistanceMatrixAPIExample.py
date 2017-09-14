# importing the requests library
import requests
 
# api-endpoint
URL = "http://maps.googleapis.com/maps/api/distancematrix/json"
 
# location given here
#orig = "Bangalore+India"
#dest = "Chennai+India"

def getDistance(origin,dest):
	#print("Getting Distance between {} and {}".format(orig,dest))
	payload = { 'origins': origin, 'destinations': dest}
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = payload )

	# extracting data in json format
	data = r.json()

	#print(r.url)
	#print(data)
	# extracting Formatted Origin Address, Destination Address, Distance and duration
	originAdd = data['origin_addresses']
	destinationAdd = data['destination_addresses']
	dist = data['rows'][0]['elements'][0]['distance']['text']
	dura = data['rows'][0]['elements'][0]['duration']['text']
	#print("Distance between them is {} and it takes {}.".format(dist,dura))
	print("Distance between %s and %s is %s and it takes %s."%(originAdd,destinationAdd,dist,dura))

	
origin= str(raw_input("Enter Origin Location.."))
dest = str(raw_input("Enter Destination Location.."))
getDistance(origin,dest)
