

import requests
import json

keyword = input("insert keyword : ")
output = open("ip.txt","a")
with open(keyword, "r") as list_file:
        for line in list_file:
                word = line.strip()
            
                headers = { 'accept': 'application/json',
                        'Authorization': 'Bearer 55f8ebe6-536f-4b59-863b-30627233bb69',
                        'Content-Type': 'application/json'
                    }
                data = '{"limit":100,"offset":0,"search_params":[],"query":"\\"'+word+'\\""}'
                url = 'https://api.spyse.com/v4/data/ip/search'
                reqs = requests.post(url,headers=headers, data=data)
                result = reqs.json()

                count = 0
                while(count <= 100):
                    data = result["data"]["items"][count]["ip"]
                    print(data)
                    output.write(data+"\n")
                    count = count+1
