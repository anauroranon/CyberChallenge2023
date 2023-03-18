#! /usr/bin/python3

from chall import encrypt, decrypt
import os

FLAG = os.environ['FLAG']


def dump_user(user):
    def try_to_bytes(x):
        if type(x) == bytes:
            return x
        elif type(x) == str:
            return x.encode()
        else:
            return str(x).encode()
    return b"&".join(key.encode()+b"="+try_to_bytes(value) for key, value in user.items())


def load_user(user):
    try:
        fields = user.split(b'&')
        object = {}
        for field in fields:
            k, v = field.split(b'=')
            object[k.decode()] = v.strip()
        return object
    except:
        return None


def start_server():
    username = input("Hello! What's your name? ")
    if '=' in username or '&' in username:
        print("Don't know the guy.")
        exit(-1)

    user = {"username": username, "admin": b"False"}
    cookie_pt = dump_user(user)

    ct = encrypt(cookie_pt)
    print("Here's your cookie, keep it safe!", ct.decode())

    new_ct = input("Wait, I forgot something, can you give it back please? ")
    pt = decrypt(new_ct)

    user = load_user(pt)
    if user == None:
        print("Invalid cookie.")

    if user['admin'] == b'True':
        print("Thank you admin!", FLAG)
    else:
        print("Thank you, have a nice day :)")


if __name__ == "__main__":
    start_server()
