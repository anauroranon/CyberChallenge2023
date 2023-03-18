#! /usr/bin/python3

from Crypto.Random import random
from chall import encrypt, STRING_SIZE, WINS_NEEDED, TRIES
from utils import input_bits, bits_to_string
import os

FLAG = os.environ['FLAG']


def start_server():
    wins = 0
    # Get the two plaintexts
    xs = []
    xs.append(input_bits("Give me an x0: ", STRING_SIZE))
    xs.append(input_bits("Give me an x1: ", STRING_SIZE))

    # Generate which plaintexts will be encrypted
    bs = [random.randint(0, 1) for _ in range(TRIES)]

    # Encrypt them
    cs = [encrypt(xs[b]) for b in bs]

    # Output the ciphertexts
    print("Here you go:", ", ".join(bits_to_string(c) for c in cs))

    # Get the guesses
    guess = input("Guess: ")
    guesses = [int(guess.strip()) for guess in guess.split(',')]
    if any(guess != 0 and guess != 1 for guess in guesses):
        print("There are only two plaintexts.")
        exit(-1)
    if len(guesses) != TRIES:
        print("You didn't guess the right amount of challenges.")
        exit(-1)

    # Calculate the results
    results = [b == guess for b, guess in zip(bs, guesses)]
    wins = sum(results)

    if wins >= WINS_NEEDED:
        print(f"You deserve this:", FLAG)
    else:
        print(f"Not good enough. {wins}/{WINS_NEEDED} (out of {TRIES})")


if __name__ == "__main__":
    start_server()
