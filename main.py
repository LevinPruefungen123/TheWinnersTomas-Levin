import variables
import moveTo
import getResources
import sellResources
import sortInventory
import time
import requests


def automatedIron():
    while True:
        moveTo.setTargetByStation("Vesta Station")
        while True:
            if moveTo.stationInReach("Vesta Station") == True:
                sortInventory.fillInventory(5, "IRON")
                break
            
        moveTo.setTargetByStation("Core Station")
        while True:
            if moveTo.stationInReach("Core Station") == True:
                time.sleep(3)
                sellResources.sellIron()
                break


def goBack():
    moveTo.setTargetByStation("idle")
    requests.put("http://192.168.100.13:2004/thruster", '{"thrust_percent" : 40}')
    time.sleep(1)
    requests.put("http://192.168.100.13:2004/thruster", '{"thrust_percent" : 0}')

def automatedPlatin():
    while True:
        moveTo.setTargetByCords(50233,77426)
        while True:
                time.sleep(5)
                goBack()
                sortInventory.fillInventory(5, "PLATINUM")
                break
            
        moveTo.setTargetByStation("Core Station")
        while True:
            if moveTo.stationInReach("Core Station") == True:
                time.sleep(3)
                sellResources.sellPlatin()
                break


automatedIron()