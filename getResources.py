import requests
import time
import variables

def buyResource(payload):
    requests.post(variables.buyResourceURL, json=payload)

def getResourceLaser(resource):
    amountLaserBeams = 0
    if resource == "GOLD" or resource == "PLATINUM": 
        amountLaserBeams = 14
    if resource == "CHRONOTIT": 
        amountLaserBeams = 1
    if resource == "FRAGILON": 
        amountLaserBeams = 20
    if resource == "MAGNON": 
        amountLaserBeams = 2
    if resource == "QUEST":
        amountLaserBeams = 40

    index = 0
    while index < amountLaserBeams: 
        print("Laser reactivated")
        requests.post(variables.activateLaserURL)        
        time.sleep(8)
        index += 1
    

