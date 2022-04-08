import urllib.request
url_ = input("Enter website to scan:")
v = open("link.txt" , "r" )
while True:
    panel = v.readline()      
    if not panel:
        break
    url = "https://"+url_+"/"+panel
    try :
        f = urllib.request.urlopen(url)
        f.addheaders (["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"])

    except urllib.error.URLError as e :
        print("An error occured \n Status :"+str(e.status)+":"+e.msg +"\n Try the following : \n 1. Input a valid web address in a valid format e.g me.com \n 2. Make sure you have an internet connection.")
    except urllib.error.HTTPError as e:
        print("An error occured \n Status :"+str(e.status)+":"+e.status_code +"\n Try the following : \n 1. Input a valid web address in a valid format e.g me.com \n 2. Make sure you have an internet connection.")
    else:
        print("Status : " + str(e.status) +":"+ e.status_code) 
        print ("Admin panel found: => ",url)
