import requests
response = requests.get("https://api.github.com/repos/4yeesnice/1stproject/commits",headers={'Authorization':'Token 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'}).json()
i = 0
k = 0
list = []
for r in response:
    i+=1
    list.append(r["commit"]['message'])
    if len(r["commit"]['message'])>10:
        k+=1
print(i,k)
print(list)
name_list = []
for i in response:
    if i['commit']['author']['name'] not in name_list:
        name_list.append(i['commit']['author']['name'])
print(name_list)
for name in name_list:
    i = 0
    for r in response:
        if name in r['commit']['author']['name']:
            i+=1
    total = {
        name:i
    }
    print(total)