
def directions():
        import urllib.request
        import json
        endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

        API_KEY = 'AIzaSyBeyL_F1aE_b4Xs7udR8KtshNicavmt4vU'

        origin = input('Where are you?: ').replace(' ','+')
        destination = 'The+University+Of+British+Columbia+Okanagan'

        nav_request = 'origin='+origin+'&destination='+destination+'&key='+API_KEY
        request = endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        directions = json.loads(response)
        routes = directions['routes']
        legs=routes[0]['legs']
        print('The routes you can take are: '+routes[0]['summary']+'; The distance is: '+legs[0]['distance']['text'])


directions()


