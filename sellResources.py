import variables
import requests
 
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