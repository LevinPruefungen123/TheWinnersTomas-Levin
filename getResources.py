import requests
import time
import variables

def buyResource(payload):
    requests.post(variables.buyResourceURL, json=payload)

def getResourceLaser(resource):
    if resource == "GOLD" or resource == "PLATINUM": 
        amountLaserBeams = 8
    if resource == "CHRONOTIT": 
        amountLaserBeams = 3

    index = 0
    while index < amountLaserBeams: 
        requests.post(variables.activateLaserURL)        
        time.sleep(8)
        requests.post(variables.deactivateLaserURL)
        index += 1
    

