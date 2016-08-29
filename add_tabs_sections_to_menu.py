#!/usr/bin/python3

import simplejson as json
import sys

def addTabs(data):
    text =''' { "allTheTabs": {
    "LandUse": { "title": "Land Use", "order": 0, "isActive": true, "redact": false, "permissions": null },
    "CityInfo": { "title": "City Info", "order": 2, "isActive": false, "redact": false, "permissions": null },
    "Development": { "title": "Development", "order": 1, "isActive": false, "redact": false, "permissions": null },
    "Incentives": { "title": "Incentives", "order": 3, "isActive": false, "redact": false, "permissions": null },
    "WDCEP": { "title": "WDCEP", "order": 4, "isActive": false, "redact": false, "permissions": "layer.tab.WDCEP" },
    "InPatient": { "title": "In Patient", "order": 5, "isActive": false, "redact": false, "permissions": "group.tab.Array" },
    "ParkHeights": { "title": "Park Heights", "order": 6, "isActive": false, "redact": false, "permissions": null }
  }}'''
    newTabs = json.loads(text)
    data["allTheTabs"] = newTabs["allTheTabs"]
    
    return data

def addSections(data):
    text = ''' {
      "allTheSections": {
    "LandUse1": { "title": "Land Use & Entitlement", "order": 0, "redact": false, "permissions": null, "parentTab": "LandUse" },
    "LandUse2": { "title": "Overlay Zones", "order": -1, "redact": false, "permissions": null, "parentTab": "LandUse" },
    "LandUse3": { "title": "Historic Districts", "order": 2, "redact": false, "permissions": null, "parentTab": "LandUse" },
    "LandUse4": { "title": "Heatmaps", "order": 0, "redact": false, "permissions": null, "parentTab": "LandUse" },
    "LandUse5": { "title": "Natural Hazards", "order": 0, "redact": false, "permissions": null, "parentTab": "LandUse" },
    "CityInfo1": { "title": "Geography", "order": 0, "redact": false, "permissions": null, "parentTab": "CityInfo" },
    "CityInfo2": { "title": "Amenities", "order": 0, "redact": false, "permissions": null, "parentTab": "CityInfo" },
    "Development1": { "title": "Leasing", "order": 0, "redact": false, "permissions": null, "parentTab": "Development" },
    "Development2": { "title": "Development", "order": 0, "redact": false, "permissions": null, "parentTab": "Development" },
    "Development3": { "title": "Demographics", "order": 0, "redact": false, "permissions": null, "parentTab": "Development" },
    "Incentives1": { "title": "Incentives", "order": 0, "redact": false, "permissions": null, "parentTab": "Incentives" },
    "WDCEP1": { "title": "WDCEP", "order": 0, "redact": false, "permissions": "layer.section.WDCEP", "parentTab": "WDCEP" }
  }}'''
    newSections = json.loads(text)
    data["allTheSections"] = newSections["allTheSections"]

    return data

def rewriteLayers(data):
    for item in data["allTheLayers"]:
        lyr = data["allTheLayers"][item]
        if lyr["category"] == '1' and lyr['subCategory'] == '1':
            lyr["menuSection"] = "LandUse1"
            continue
        if lyr["category"] == '1' and lyr['subCategory'] == '2':
            lyr["menuSection"] = "LandUse2"
            continue
        if lyr["category"] == '1' and lyr['subCategory'] == '3':
            lyr["menuSection"] = "LandUse3"
            continue
        if lyr["category"] == '1' and lyr['subCategory'] == '4':
            lyr["menuSection"] = "LandUse4"
            continue
        if lyr["category"] == '1' and lyr['subCategory'] == '5':
            lyr["menuSection"] = "LandUse5"
            continue

        if lyr["category"] == '2' and lyr['subCategory'] == '1':
            lyr["menuSection"] = "CityInfo1"
            continue
        if lyr["category"] == '2' and lyr['subCategory'] == '2':
            lyr["menuSection"] = "CityInfo2"
            continue

        if lyr["category"] == '3' and lyr['subCategory'] == '1':
            lyr["menuSection"] = "Development1"
            continue
        if lyr["category"] == '3' and lyr['subCategory'] == '2':
            lyr["menuSection"] = "Development2"
            continue
        if lyr["category"] == '3' and lyr['subCategory'] == '3':
            lyr["menuSection"] = "Development3"
            continue

        if lyr["category"] == '4' and lyr['subCategory'] == '1':
            lyr["menuSection"] = "Incentives1"
            continue

        if lyr["category"] == '5' and lyr['subCategory'] == '1':
            lyr["menuSection"] = "WDCEP1"
            continue

        if lyr["category"] == '6' and lyr['subCategory'] == '1':
            lyr["menuSection"] = "InPatient1"
            continue

        if lyr["category"] == '7' and lyr['subCategory'] == '1':
            lyr["menuSection"] = "ParkHeights1"
            continue

    return data

if __name__ == "__main__":

    fil = sys.argv[1]
    nfil = fil + "_new"

    with open(fil, 'r') as fh:
        data = fh.read()
        menu = json.loads(data)

    nmenu = addTabs(menu)
    nmenu = addSections(nmenu)
    nmenu = rewriteLayers(nmenu)

    with open(nfil, "w+") as fh:
        fh.write(json.dumps(nmenu, sort_keys=True, indent=4 * ' '))


