import json

data={
    "name":"Bhagya",
    "age":20,
    "Location":"Bangalore",
    "Skills":["Python","Java"]
}

with open("data.json","w") as file:
    json.dump(data,file,indent=10)
