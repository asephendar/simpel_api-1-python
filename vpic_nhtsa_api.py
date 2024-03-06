import requests, json

response = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json')
products = response.json()

def getCountry(a):
    results = []
    
    if "Results" in a:
        for el in a["Results"]:
            if "Country" in el:
                results.append({"Country": el["Country"], "Mfr_Name": el["Mfr_Name"]})
    
    return results

hasil = getCountry(products)
print(json.dumps(hasil, indent=2))
