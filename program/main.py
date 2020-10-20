from fastapi import FastAPI, HTTPException
import json


# Import Azure regions
def getRegions():
    with open("./azureRegions.json") as azure_regions_file:
        azure_regions_temp = json.load(azure_regions_file)

        azure_regions_dict = azure_regions_temp

        # Return only physical regions
        azure_regions_dict = [
            x for x in azure_regions_dict if x["metadata"]["regionType"] == "Physical"
        ]

        # Include short_code for region
        for d in azure_regions_dict:
            words = d["displayName"].split()
            letters = [word[0] for word in words]
            d["shortCode"] = ("".join(letters)).upper()
            d["shortCodeLowerCase"] = ("".join(letters)).lower()

        # Transform Python object back into JSON
        return azure_regions_dict


# Validate the region against our Azure regions
def validateRegion(region: str):
    azureRegions = getRegions()

    for r in azureRegions:
        if r["displayName"] == region:
            return r
        else:
            pass

    raise TypeError(region)


def validateResourceType(resourceType: str):
    supportedResourceTypes = {"Microsoft.Compute/virtualMachines": "VM"}

    for key in supportedResourceTypes:
        if key == resourceType:
            return supportedResourceTypes[key]
        else:
            pass

    raise TypeError(resourceType)


app = FastAPI()


@app.get("/")
async def root():
    introText = "Welcome to the Azure Naming Convention API. Browse to /docs to see what you can do."
    return {"message": introText}


@app.get("/get_name")
async def get_name(resourceType: str, region: str):
    try:
        environment = "A"
        regionDetails = validateRegion(region)
        resourceTypeDetails = validateResourceType(resourceType)
    except TypeError as e:
        raise HTTPException(status_code=400, detail=f"Input not valid: {str(e)}")

    name = environment + regionDetails["shortCode"] + resourceTypeDetails

    data = {
        "environment": environment,
        "region": regionDetails,
        "resourceType": resourceTypeDetails,
    }

    naming = {
        "name": name,
        "nameUpperCase": name.upper(),
        "nameLowerCase": name.lower(),
        "data": data,
    }

    return naming


@app.get("/get_regions")
async def get_regions():
    return getRegions()
