import json
strr = ''
x = ''
with open("/home/neeraj/Desktop/project/digital_assistant/mural.txt",'r') as ff:
    reader = ff.read()

    print(len(reader))
    for i in reader:
        if ord(i) == 160:
            continue
        else:
            strr+=i
    print(len(strr))
    x = json.loads(strr)
    print(len(x))
data = []
for xxx in x:
    try:
        pd = xxx["widget"]["parentId"]
    except:
        pd = ""
    try:

        text = xxx["content"]["text"]
    except:
        text = ""
    da = {"action":xxx["action"],"mural":xxx["mural"],"parent_id":pd,"timestamp":xxx["timestamp"],"text":text}

    data.append(da)
daaa = {
            "type":"mural",
            "entries":data
}

import requests

resp = requests.post("http://localhost:8080/ingest",data = json.dumps(daaa))
print(resp.status_code)

