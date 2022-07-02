#Geolocator
import json, urllib.request, webbrowser
ip = input("Enter the IP Address to get location: ")
api = "http://ip-api.com/json/{}".format(ip)
ipinfo = urllib.request.urlopen(api)
try :
    with open("ipinfo.json", mode = 'w' ) as f :
        f = json.load(ipinfo)
except urllib.HTTPError as e :
    print("An Error occured")
except urllib.URLError as a :
    print("An Error occured")
else :
    latitude = f['lat']
    longitude = f['lon']
    bingmap = "https://www.bing.com/maps?q=get+location+on+map+from+coordinates&FORM=HDRSC4&cp={lat}%7E{lon}&lvl=16.8&style=g&pi=18&style=a".format(lat=latitude, lon=longitude)
    webbrowser.open_new(bingmap)
