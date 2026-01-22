import requests

geturl1="http://127.0.0.1:5001/users"

headers={
    "Accept":"application/json",
    "User-Agent":"Python-Requests-Client"

}
response=requests.get(geturl1,headers=headers,timeout=10)

response=requests.get(geturl1)

print("get status code",response.status_code)
print(response.json())

post_url1="http://127.0.0.1:5001/users"
body={
    "name":"Abhi"
}
response=requests.post(post_url1,json=body)
print("post status code",response.status_code)
print(response.json())

put_url="http://127.0.0.1:5001/users/2"
body1={
    "name":"Janvi"
}
response=requests.put(put_url,json=body1)
print("put status code",response.status_code)
print(response.json())

patch_url="http://127.0.0.1:5001/users/1"
body2={
    "name":"adya"
}
response=requests.patch(patch_url,json=body2)
print("patch status code",response.status_code)
print(response.json())

delete_url="http://127.0.0.1:5001/users/2"
r4=requests.delete(delete_url)
print("delete status code",r4.status_code)
print(r4.json())
