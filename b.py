import requests
import json
import threading
import time
import random
 
#deal with config.json
 
username = input("user :")
password = input("pass: ")
#names = {'nife'}
targets = input('target :').splitlines() 
 
#this is so I can dynamically change the endpoint
endpoint = "https://www.instagram.com/<username>"
 
 
def turbo(nam):
 
    #login to instagram, create a session and get a csrf for later
    s = requests.session()
 
    print(f"[{nam}] Logging Into {username}...")
    url1 = "https://www.instagram.com/accounts/login/"
 
    r1 = s.get(url1)
 
    csrf1 = r1.cookies.get_dict()['csrftoken']
 
    url2 = 'https://www.instagram.com/accounts/login/ajax/'
 
    h2 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'x-csrftoken': csrf1,
        'x-instagram-ajax': '1',
        'x-requested-with': 'XMLHttpRequest'
    }
 
    data2 = {
        'username': username,
        'password': password,
        'queryParams': '{}'
    }
 
    r2 = s.post(url2, headers=h2, data=data2)
 
    if r2.json()['authenticated'] == False:
        print(f'[{nam}] ERROR LOGGING IN...')
        exit()
    else:
        csrf = r2.cookies.get_dict()['csrftoken']
        print(f'[{nam}] Logged In Initiating Turbo...')
        print("")
    turboin = True
    #start monitoring the username
    c = 0
    while turboin == True:
        c += 1
        res = requests.get(endpoint.replace("<username>", nam))
        if res.status_code == 404:
            print(f'[{nam}] NAME AVAILABLE TAKING IT')
            urlf = "https://www.instagram.com/accounts/edit/"
 
            hf = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/edit/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                'x-csrftoken': csrf,
                'x-instagram-ajax': '1',
                'x-requested-with': 'XMLHttpRequest'
            }
 
            df = {
                'first_name': 'Nayef',
                'email': "{}test@nayef.online".format(str(random.randint(11111111, 99999999))),
                'username': nam,
                'phone_number':'',
                'gender': '3',
                'biography':'',
                'external_url':'',
                'chaining_enabled': 'on'
            }
            #change the acc to the turbo name
            rf = s.post(urlf, headers=hf, data=df)
            print(f'[{nam}] Completed Turbo Killing Thread')
            turboin = False
        else:
            print("({}) [{}] Name Unavailable <{}>".format(str(c), nam, res.status_code))
            print("")
 
 
if __name__ == '__main__':
    print("INSTATURBO")
    print("-" * 30)
    print(f"Username: {username}")
    print("Password: {}".format("*" * len(password)))
    print("# Of Targets: {}".format(str(len(targets))))
    print(f"Endpoint: {endpoint}")
    print("-" * 30)
    print("")
    tin = input("Would you like to start (y/n)?: ")
    if tin.lower() == "y":
        for x in targets:
            #print(x)
            t = threading.Thread(target=turbo, args=(x, ))
            t.start()
    else:
        exit()
