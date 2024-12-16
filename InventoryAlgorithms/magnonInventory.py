import requests
import variables
import getResources
import time

def swap_adjacent(a, b): 
    response = requests.post(variables.cargoSwapAdjacentURL, json={"a": a, "b": b}) # swaps the two spots
    return response.json()

def buyOrGetResource(resource):
    if resource == "IRON": 
        getResources.buyResource(variables.payloadBuySell("Vesta Station", "IRON", 12))
    elif resource == "GOLD" or resource == "PLATINUM" or resource == "CHRONOTIT" or resource == "FRAGILON" or "MAGNON": 
        getResources.getResourceLaser(resource)


def sortMagnonRow(resource, maxRow, amountRows):
    # buy one Chronotit
    current_x = 12
    current_y = 0
    
    while current_x >= 1: 
        swap_response = swap_adjacent({"x": current_x, "y": current_y}, {"x": current_x - 1, "y": current_y})
        current_x -= 1
        if swap_response["kind"] != "success":
            print("Failed to swap items", swap_response)
            break
        time.sleep(0.4)

def sendMagnonDown(row): 
    current_x, current_y = 0
    while current_y <= row:
        swap_response = swap_adjacent({"x": current_x, "y": current_y}, {"x": current_x, "y": current_y - 1})
        current_y += 1
        if swap_response["kind"] != "success":
            print("Failed to swap items", swap_response)
            break
        time.sleep(0.4)

def sendMagnonToRestingSpot(row, amountRows):
    current_x = 0
    current_y = row







def sortInv(amountRows, resource):
 
    while index >= amountRows:
        if firstRow:
            buyOrGetResource(resource)
            firstRow = False
        if current_x >= 12:
            current_x = 0
            current_y += 1

        if current_y >= maxRow:
            maxRow -= 1
            buyOrGetResource(resource)
        
        if maxRow == 1: 
            break

        if current_y > 0:
            swap_response = swap_adjacent({"x": current_x, "y": current_y}, {"x": current_x, "y": current_y - 1})
            if swap_response["kind"] != "success":
                print("Failed to swap items", swap_response)
                break

        index += 1
