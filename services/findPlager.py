import requests
url="https://www.editpad.org/plag_req_v5"
data="fuck"
API_KEY="5cec2091350e7a1d8e1f2bd281756b962dcea5d8"


data=f"{API_KEY}&{data}"
response = requests.post(url, data=data)

test=response.json()
print(test)

    
    


    