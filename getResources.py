import requests
import time
import variables

def buyResource(payload):
    requests.post(variables.buyResourceURL, json=payload)

def getResourceLaser(resource):
    if resource == "GOLD" or resource == "PLATINUM": 
        amountLaserBeams = 7
    if resource == "CHRONOTIT": 
        amountLaserBeams = 1
    if resource == "FRAGILON": 
        amountLaserBeams = 10

    index = 0
    while index < amountLaserBeams: 
        requests.post(variables.activateLaserURL)        
        time.sleep(9)
        requests.post(variables.deactivateLaserURL)
        index += 1
    

