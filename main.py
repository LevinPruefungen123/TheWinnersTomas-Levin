import moveTo
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
    requests.put("http://192.168.100.13:2004/thruster", '{"thrust_percent" : 25}')
    time.sleep(0.7)
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

def automatedChronotit():
    while True:
        moveTo.setTargetByCords(39006, 38652)
        time.sleep(75)
        while True: 
            time.sleep(5)
            goBack()
            sortInventory.fillInventory(8, "CHRONOTIT")
            break

        moveTo.setTargetByStation("Core Station")
        while True: 
            if moveTo.stationInReach("Core Station") == True: 
                time.sleep(6)
                sellResources.sellChronotit()
                break

def automatedFragilon():
    while True:
        moveTo.setTargetByCords(45081, -40991)
        time.sleep(20)
        while True: 
            time.sleep(5)
            goBack()
            sortInventory.fillInventory(2, "FRAGILON")
            break
        
        moveTo.setTargetByStation("Core Station")
        while True:
            if moveTo.stationInReach("Core Station") == True:
                time.sleep(10)
                sellResources.sellFragilon()
                break

automatedFragilon()