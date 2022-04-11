import urllib.request
url_ = input("Enter website to scan:")
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
v = open("link.txt" , "r" )
while True:
    panel = v.readline()      
    if not panel:
        break
    url = "https://"+url_+"/"+panel
    try :
        f = urllib.request.urlopen(url)
        #f.addheaders(headers)

    except urllib.error.URLError as e :
        print("An error occured \n Status :"+str(e.status)+":"+e.msg +"\n Try the following : \n 1. Input a valid web address in a valid format e.g me.com \n 2. Make sure you have an internet connection.")
    except urllib.error.HTTPError as e:
        print("An error occured \n Status :"+str(e.status)+":"+e.status_code +"\n Try the following : \n 1. Input a valid web address in a valid format e.g me.com \n 2. Make sure you have an internet connection.")
    else:
        print("Status : " + str(f.msg) +":"+ str(f.code)) 
        print ("Admin panel found: => ",url)
        break
