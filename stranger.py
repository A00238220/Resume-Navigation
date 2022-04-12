import urllib.request
import json
import random
import time

def get_advice():
    print("You see the stranger, and he has some advice for you!\n")
    time.sleep(2)
    url = f'https://raw.githubusercontent.com/SidneyCodes/advice/master/advice.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print(result[random.randint(1,50)]['advice'])
    time.sleep(2)
    print()

    