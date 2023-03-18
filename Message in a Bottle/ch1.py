
ciphertext = "SHGDDGLZAJLWWFOSKLZWKWNWFLZESFFWVEAKKAGFAFLZWSHGDDGKHSUWHJGYJSESFVLZWLZAJVAFLWFVWVLGDSFVGFLZWEGGFLZWUJSXLOSKDSMFUZWVXJGELZWCWFFWVQKHSUWUWFLWJXDGJAVSTMLLZWDMFSJDSFVAFYOSKSTGJLWVSXLWJSFGPQYWFLSFCWPHDGVWVLOGVSQKDSLWJUJAHHDAFYLZWKWJNAUWEGVMDWMHGFOZAUZLZWUGEESFVEGVMDWZSVVWHWFVWV"

def shift_cipher_dec (N, cipertext):
    for k in range(1, N+1):
        plaintext = ""
        for char in range(len(cipertext)):
            ascii = ord(cipertext[char])
            transformation = (ascii - k)

            if transformation < 65:
                transformation += 26

            plaintext += chr(transformation)

        print ("\n"+plaintext)

# shift_cipher_dec(26, ciphertext)



