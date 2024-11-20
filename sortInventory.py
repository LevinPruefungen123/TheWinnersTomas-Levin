import requests
import variables
import time
import getResources

def swap_adjacent(a, b): 
    response = requests.post(variables.cargoSwapAdjacentURL, json={"a": a, "b": b}) # swaps the two spots
    return response.json()

def get_hold_structure():
    response = requests.get(variables.cargoStructureURL)
    return response.json() # returns structure of cargo

def buyOrGetResource(resource):
    if resource == "IRON": 
        getResources.buyResource(variables.payloadBuySell("Vesta Station", "IRON", 12))
    elif resource == "GOLD" or resource == "PLATINUM" or resource == "CHRONOTIT" or resource == "FRAGILON": 
        getResources.getResourceLaser(resource)

def fillInventory(maxRow1, resource):
    current_x, current_y = 0, 1
    items_bought = 0
    maxRow = maxRow1
    amountItemsToBuy = maxRow * 12

    buyOrGetResource(resource)
    while items_bought < amountItemsToBuy: 
        print("in while")
        if current_x >= 12:
            current_x = 0
            current_y += 1
        
        if current_y >= maxRow:
            maxRow -= 1
            current_x, current_y = 0, 1
            buyOrGetResource(resource)
            

        if maxRow == 1: 
            break

        # in this if statement (if y is bigger than 0) the two slots will get switched (it moves one y down)    
        if current_y > 0:
            swap_response = swap_adjacent({"x": current_x, "y": current_y}, {"x": current_x, "y": current_y -1})
            if swap_response["kind"] != "success":
                print("Failed to swap items", swap_response)
                break

        time.sleep(0.45)       
        current_x += 1
