import moveTo
import sellResources
import sortInventory
import time
import requests
import energyManagement
import topSecret
import asyncio
import getResources

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
    requests.put("http://192.168.100.13:2004/thruster", '{"thrust_percent" : 24}')
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

def automatedChronotit():
    while True:
        moveTo.setTargetByCords(39006, 38652)
        time.sleep(80)
        while True: 
            goBack()
            time.sleep(7)
            sortInventory.fillInventory(5, "CHRONOTIT")
            break

        moveTo.setTargetByStation("Core Station")
        while True: 
            if moveTo.stationInReach("Core Station") == True: 
                time.sleep(6)
                sellResources.sellChronotit()
                break

def automatedFragilon():
    while True:
        energyManagement.main(energyManagement.new_limits_flying)
        moveTo.setTargetByCords(45081, -40991)
        time.sleep(10)
        while True:
            goBack()
            time.sleep(5)
            sortInventory.fillInventory(3, "FRAGILON")
            break
        
        asyncio.run(sellFragilon())

def automatedMagnon(): 
    energyManagement.main(energyManagement.new_limits_flying)
    moveTo.setTargetByCords(-55850, -58879)
    time.sleep(100)

    while True:
        goBack()
        time.sleep(5)
        sortInventory.fillInventory(4, "MAGNON")
        break
    energyManagement.main(energyManagement.new_limits_flying)
    moveTo.setTargetByStation("Core Station")
    time.sleep(100)
    energyManagement.main(energyManagement.new_limits_selling_buying)
    sellResources.sellMagnon()


async def sellFragilon():
    energyManagement.main(energyManagement.new_limits_reactor)
    time.sleep(6)
    energyManagement.main(energyManagement.new_limits_charging)
    time.sleep(250)
    await topSecret.main(30000, -30000)
    time.sleep(250)
    await topSecret.main(15000, -20000)
    time.sleep(250)
    await topSecret.main(0, -20000)
    time.sleep(250)
    await topSecret.main(0, 0)
    energyManagement.main(energyManagement.new_limits_selling_buying)
    sellResources.sellFragilon()
                


if __name__ == "__main__":
    while True:
        automatedMagnon()

