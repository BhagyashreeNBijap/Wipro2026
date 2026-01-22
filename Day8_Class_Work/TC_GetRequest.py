import requests
from requests import delete

geturl="https://api.restful-api.dev/objects"

response=requests.get(geturl)

print("get status code",response.status_code)
print(response.json())

posturl="https://api.restful-api.dev/objects"

body1={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

r1=requests.post(posturl,json=body1);
print("post status code",r1.status_code)
print(r1.json())


geturl1="https://api.restful-api.dev/objects?id=3&id=5&id=10"
r2=requests.get(geturl1);
print("gwt status code",r2.status_code)
print(r2.json())

geturl2="https://api.restful-api.dev/objects/7"
r3=requests.get(geturl2);
print("get status code",r3.status_code)
print(r3.json())

puturl="https://api.restful-api.dev/objects/ff8081819782e69e019be421d8b12f45"

body2={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}
r4=requests.put(puturl,json=body2);
print("put status code",r4.status_code)
print("put status code",r4.status_code)
print(r4.json())

patchurl="https://api.restful-api.dev/objects/ff8081819782e69e019be427954e2f70"
body3={
   "name": "Apple MacBook Pro 16 (Updated Name)"
}

r5=requests.patch(patchurl,json=body3);
print("patch status code",r5.status_code)
print(r5.json())

delete_url="https://api.restful-api.dev/objects/ff8081819782e69e019be427954e2f70"
r6=requests.delete(delete_url)
print("delete status code",r6.status_code)
print(r6.json())

