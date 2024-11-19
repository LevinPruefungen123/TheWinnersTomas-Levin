team = open('C:\\Users\\Public\\Documents\\whatGroup.txt').read().strip()
# Variables for all code
if team == "LevinTomas":
    # Easy steering
    easySteeringURL = "http://192.168.100.13:2009/set_target"

    payloadIdle = {"target": "idle"}
    payloadStop = {"target": "stop"}
    payloadCoreStation = {"target": "Core Station"}
    payloadVestaStation = {"target": "Vesta Station"}
    payloadAzuraStation = {"target": "AzuraStation"}
    def payloadDynamyc(station):
        return {"target": station}
    def payloadCoordinates(x, y):
        return {"x": x, "y": y}

    # Laser
    activateLaserURL =  "http://192.168.100.13:2018/activate"
    deactivateLaserURL = "http://192.168.100.13:2018/deactivate"

    # Buy / Sell
    sellingURL = "http://192.168.100.13:2011/sell"
    buyResourceURL = "http://192.168.100.13:2011/buy"
    buyItemURL = "http://192.168.100.13:2011/buy_item"
    def payloadBuySell(station, resource, amount): 
        return {"station": station, "what": resource, "amount": amount}
    def payloadItem(station, item):
        return {"station": station, "what": item} 
    
    # Stations
    stationsInReachURL = "http://192.168.100.13:2011/stations_in_reach"
    shipPositionURL = "http://192.168.100.13:2011/pos"

    # Cargo 
    cargoStructureURL = "http://192.168.100.13:2012/structure"
    cargoSwapAdjacentURL = "http://192.168.100.13:2012/swap_adjacent"
    
if team == "MoritzDan":
    # Easy steering
    easySteeringURL = "http://192.168.100.14:2009/set_target"

    payloadIdle = {"target": "idle"}
    payloadStop = {"target": "stop"}
    payloadCoreStation = {"target": "Core Station"}
    payloadVestaStation = {"target": "Vesta Station"}
    payloadAzuraStation = {"target": "AzuraStation"}
    def payloadDynamyc(station):
        return {"target": station}
    def payloadCoordinates(x, y):
        return {"x": x, "y": y}

    # Laser
    activateLaserURL =  "http://192.168.100.14:2018/activate"
    deactivateLaserURL = "http://192.168.100.14:2018/deactivate"

    # Buy / Sell
    sellingURL = "http://192.168.100.14:2011/sell"
    buyResourceURL = "http://192.168.100.14:2011/buy"
    buyItemURL = "http://192.168.100.14:2011/buy_item"
    def payloadBuySell(station, resource, amount): 
        return {"station": station, "what": resource, "amount": amount}
    def payloadItem(station, item):
        return {"station": station, "what": item} 
    
    # Stations
    stationsInReachURL = "http://192.168.100.14:2011/stations_in_reach"
    shipPositionURL = "http://192.168.100.14:2011/pos"

    # Cargo 
    cargoStructureURL = "http://192.168.100.14:2012/structure"
    cargoSwapAdjacentURL = "http://192.168.100.14:2012/swap_adjacent"




