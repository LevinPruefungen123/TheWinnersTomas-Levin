import variables
import requests
import time
 
def sellIron():
    index = 0
    while index < 12:
        requests.post(variables.sellingURL, json=variables.payloadBuySell("Core Station", "IRON", 12))
        index += 1


def sellPlatin():
    index = 0
    while index < 12:
        requests.post(variables.sellingURL, json=variables.payloadBuySell("Core Station", "PLATIN", 12))
        requests.post(variables.sellingURL, json=variables.payloadBuySell("Core Station", "IRON", 12))
        requests.post(variables.sellingURL, json=variables.payloadBuySell("Core Station", "STONE", 12))
        index += 1

def sellChronotit():
    index = 0
    while index < 12:
        requests.post(variables.sellingURL, json=variables.payloadBuySell("Core Station", "CHRONOTITE", 12))
        index += 1

def sellFragilon():
    index = 0
    while index < 12:
        requests.post(variables.sellingURL, json=variables.payloadBuySell("Core Station", "FRAGILON", 12))
        index += 1

def sellMagnon(): 
    index = 0 
    while index < 12:
        requests.post(variables.sellingURL, json=variables.payloadBuySell("Core Station", "MAGNON", 12))
        requests.post(variables.sellingURL, json=variables.payloadBuySell("Core Station", "STONE", 12))
        index += 1