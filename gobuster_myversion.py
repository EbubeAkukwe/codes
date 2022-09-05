#getting pages
import requests

subdomain = []

with open("./wordlists/wordlist", 'r') as f :
    for line in f :
        x = line.strip()
        subdomain.append(x)

def main() :
    count = 0
    for k in subdomain :
        if k != "" :
            count += 1
    subdomain_len = count
    v = 0
    while subdomain_len > 0:
        full_url = ("http://10.10.15.79?api={}.img.php".format(subdomain[v]))
        v +=1
        r = requests.get(full_url)
        r_ = str(r.status_code)
        if r_ == "200" :
            print(full_url)
        if v == subdomain_len :
            break
main()
